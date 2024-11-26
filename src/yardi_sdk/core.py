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


class Client:
    def __init__(self, wsdl: str = os.getenv("WSDL_URL"), username: str = os.getenv("USERNAME"), password: str = os.getenv("PASSWORD"), log_level=logging.ERROR):
        logging.getLogger("zeep").setLevel(log_level)

        session = Session()
        session.auth = HTTPBasicAuth(username, password)
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
            return Response(response, raw_output=raw_output)
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
        """Pretty-print XML response to terminal or file."""
        xml_string = ET.tostring(self.response, encoding="utf-8", method="xml").decode("utf-8")
        pretty_xml = minidom.parseString(xml_string).toprettyxml()

        if path:
            with open(path, "w") as f:
                f.write(pretty_xml)
        else:
            print(pretty_xml)

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