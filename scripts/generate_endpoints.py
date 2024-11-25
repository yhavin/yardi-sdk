import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import logging

from zeep import Client as ZeepClient
from dotenv import load_dotenv

from yardi_sdk import type_map


load_dotenv()

class EndpointGenerator:
    def __init__(self, wsdl: str, interface: str, log_level=logging.ERROR):
        logging.getLogger("zeep").setLevel(log_level)
        
        self.client = ZeepClient(wsdl=wsdl)
        self.interface = interface

    def generate(self, output_file: str):

        explicitly_required_parameters = {"UserName", "Password", "ServerName", "Database", "Platform", "InterfaceEntity", "InterfaceLicense", "YardiPropertyId"}

        with open(output_file, "w") as f:
            for service in self.client.wsdl.services.values():
                for port_name, port in service.ports.items():
                    if "Soap12" not in port_name:  # Avoid re-running for SOAP 1.2
                        for endpoint, schema in port.binding._operations.items():
                            f.write(f"class {endpoint}:\n")
                            f.write(f'    """Interface: {self.interface}."""\n')

                            required_parameters = []
                            optional_parameters = []

                            parameters = list(schema.input.body.type.elements)
                            if parameters:
                                for parameter, parameter_type in parameters:
                                    is_optional = getattr(parameter_type, "min_occurs", 1) == 0
                                    parameter_type = self._map_parameter_type(parameter_type.type)

                                    if parameter in explicitly_required_parameters or not is_optional:
                                        required_parameters.append((parameter, parameter_type))
                                    else:
                                        optional_parameters.append((parameter, parameter_type))

                                f.write("    def __init__(\n")
                                f.write("        self,\n")

                                for parameter, parameter_type in required_parameters:
                                    f.write(f"        {parameter}: {parameter_type},\n")
                                for parameter, parameter_type in optional_parameters:
                                    f.write(f"        {parameter}: {parameter_type} = None,\n")

                                f.seek(f.tell() - 2)
                                f.write("\n    ):\n")

                                for parameter, _ in required_parameters + optional_parameters:
                                    f.write(f"        self.{parameter} = {parameter}\n")
                            else:
                                f.write("    def __init__(self):\n")
                                f.write("        pass\n")

                            f.write("\n\n")

        print(f"Endpoint schema classes generated and saved to {output_file}")

    def _map_parameter_type(self, parameter_type):
        return type_map.get(type(parameter_type), "str")
    

if __name__ == "__main__":
    bp_wsdl = os.getenv("BP_WSDL_URL")
    vi_wsdl = os.getenv("VI_WSDL_URL")
    cd_wsdl = os.getenv("CD_WSDL_URL")
    generator = EndpointGenerator(bp_wsdl, "Billing and Payments").generate(output_file="src/yardi_sdk/endpoints/billing_and_payments.py")
    generator = EndpointGenerator(vi_wsdl, "Vendor Invoicing").generate(output_file="src/yardi_sdk/endpoints/vendor_invoicing.py")
    generator = EndpointGenerator(cd_wsdl, "Common Data").generate(output_file="src/yardi_sdk/endpoints/common_data.py")