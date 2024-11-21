import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import logging

from zeep import Client as ZeepClient
from dotenv import load_dotenv

from yardi_sdk.utils import type_map


load_dotenv()

class EndpointGenerator:
    def __init__(self, wsdl: str):
        self.client = ZeepClient(wsdl=wsdl)

    def generate(self, output_file: str = "src/yardi_sdk/endpoints.py", log_level=logging.ERROR):
        logging.getLogger("zeep").setLevel(log_level)

        with open(output_file, "w") as f:
            for service in self.client.wsdl.services.values():
                for port_name, port in service.ports.items():
                    if "Soap12" not in port_name:  # Avoid re-running for SOAP 1.2
                        for endpoint, schema in port.binding._operations.items():
                            f.write(f"class {endpoint}:\n")
                            f.write("    def __init__(\n")
                            f.write("        self,\n")

                            parameters = list(schema.input.body.type.elements)
                            if parameters:
                                for parameter, parameter_type in parameters:
                                    parameter_type = self._map_parameter_type(parameter_type.type)
                                    f.write(f"        {parameter}: {parameter_type},\n")
                                f.seek(f.tell() - 2)
                                f.write("\n    ):\n")
                                for parameter, _ in parameters:
                                    f.write(f"        self.{parameter} = {parameter}\n")
                            else:
                                f.write("\n    ):\n        pass\n")

                            f.write("\n\n")

        print(f"Endpoint schema classes generated and saved to {output_file}")

    def _map_parameter_type(self, parameter_type):
        return type_map.get(type(parameter_type), "str")
    

if __name__ == "__main__":
    wsdl = os.getenv("WSDL_URL")
    generator = EndpointGenerator(wsdl)
    generator.generate()