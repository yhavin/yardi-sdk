"""
Core classes for Yardi SOAP client and API responses.

Author: Yakir Havin
"""


import logging
import lxml.etree as ET
from xml.dom import minidom
import re
import os

from zeep import Client as ZeepClient
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv


load_dotenv()


def pretty(raw: bytes | str | None) -> str | None:
    if raw is None:
        return None
    if isinstance(raw, bytes):
        raw = raw.decode("utf-8")
    try:
        return minidom.parseString(raw).toprettyxml()
    except Exception:
        return raw
    

def make_debug_hook(debug_to: str | list[str]):
    def hook(response, *args, **kwargs) -> None:
        pretty_request = pretty(response.request.body)
        pretty_response = pretty(response.content)

        if pretty_request is None:
            return

        if debug_to == "print":
            print("--- REQUEST ---")
            print(pretty_request)
            print("\n")
            print("--- RESPONSE ---")
            print(pretty_response)
        else:
            with open(debug_to[0], "w") as f:
                f.write(pretty_request)
            with open(debug_to[1], "w") as f:
                f.write(pretty_response)
    return hook


class Client:
    def __init__(
            self,
            wsdl: str = os.getenv("WSDL_URL"),
            username: str = os.getenv("USERNAME"),
            password: str = os.getenv("PASSWORD"),
            log_level=logging.ERROR,
            debug_to: str | list[str] | None = None
        ):
        logging.getLogger("zeep").setLevel(log_level)

        if debug_to is not None:
            if isinstance(debug_to, list):
                if len(debug_to) != 2 or not all(isinstance(path, str) for path in debug_to):
                    raise ValueError("`debug_to` must be a list of exactly two strings: request path and response path")
                if debug_to[0] == debug_to[1]:
                    name, _, extension = debug_to[1].rpartition(".")
                    debug_to[1] = f"{name}1.{extension}" if extension else f"{debug_to[1]}1"
            elif debug_to != "print":
                raise ValueError("`debug_to` must be 'print' or a list of two file path strings")

        self.wsdl = wsdl
        session = Session()
        session.auth = HTTPBasicAuth(username, password)
        if debug_to is not None:
            session.hooks["response"].append(make_debug_hook(debug_to))
        transport = Transport(session=session)
        self.client = ZeepClient(wsdl=wsdl, transport=transport)

    def call(self, endpoint, raw_output=False):
        """Call a Yardi endpoint."""
        endpoint_name = endpoint.__class__.__name__

        if not hasattr(self.client.service, endpoint_name):
            masked_wsdl = self._mask_wsdl(self.wsdl)
            raise ValueError(f"Endpoint '{endpoint_name}' not found. You may be using the wrong WSDL interface (using {masked_wsdl})")
        
        parameters = {key: value for key, value in endpoint.__dict__.items()}

        try:
            response = getattr(self.client.service, endpoint_name)(**parameters)
            if isinstance(response, ET._Element):
                return Response(response, raw_output=raw_output)
            else:
                return response
        except Exception as e:
            raise Exception(f"Error calling {endpoint_name}: {e}")
        
    @staticmethod
    def _mask_wsdl(wsdl: str):
        """Mask account section of WSDL URL."""
        return re.sub(r"(https?://[^/]+/)[^/]+", r"\1*****", wsdl)
        

class Response:
    def __init__(self, response: ET._Element, raw_output: bool):
        if not isinstance(response, ET._Element):
            raise ValueError("Response is not an lxml Element instance.")
        
        self.response = response

        if not raw_output:
            self._remove_namespaces()
        
    def _remove_namespaces(self):
        """Remove namespaces from XML response."""
        for element in self.response.iter():
            if "}" in element.tag:
                element.tag = element.tag.split("}", 1)[1]
        return self.response

    def dump(self, path=None):
        """
        Return pretty XML response or output to terminal or file.

        - If path is None, return pretty_xml
        - If path is "print", print to terminal
        - If path is a file path, output to file
        """
        xml_string = ET.tostring(self.response, encoding="utf-8", method="xml").decode("utf-8")
        pretty_xml = minidom.parseString(xml_string).toprettyxml()

        if path is None:
            return pretty_xml
        elif path == "print":
            print(pretty_xml)
        else:
            with open(path, "w") as f:
                f.write(pretty_xml)

    def inspect(self, path=None):
        """Print XML object structure to terminal or file."""
        structure = self._generate_structure(self.response)

        if path:
            with open(path, "w") as f:
                f.write("\n".join(structure))
        else:
            print("\n".join(structure))

    def _generate_structure(self, xml_element: ET._Element, parent_path="", level=0, seen_paths=None):
        """Recursively generate XML object structure (with a list marker for repeating objects)."""
        if seen_paths is None:
            seen_paths = set()

        structure = []
        indent = "    " * level
        current_path = f"{parent_path}/{xml_element.tag}" if parent_path else xml_element.tag

        sample_value = xml_element.text.strip() if xml_element.text and xml_element.text.strip() else None
        value_string = f": {sample_value}" if sample_value else ""

        if xml_element.getparent() is not None:
            is_list = len(xml_element.getparent().findall(xml_element.tag)) > 1
        else:
            is_list = False

        list_marker = " [List]" if is_list else ""

        if current_path not in seen_paths:
            seen_paths.add(current_path)
            structure.append(f"{indent}{xml_element.tag}{list_marker}{value_string}")

        for child in xml_element:
            structure.extend(self._generate_structure(child, current_path, level + 1, seen_paths))

        return structure