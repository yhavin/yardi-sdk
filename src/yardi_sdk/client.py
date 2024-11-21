import logging

from zeep import Client as ZeepClient
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth


class Client:
    def __init__(self, wsdl: str, username: str, password: str, log_level=logging.ERROR):
        logging.getLogger("zeep").setLevel(log_level)

        session = Session()
        session.auth = HTTPBasicAuth(username, password)
        transport = Transport(session=session)
        self.client = ZeepClient(wsdl=wsdl, transport=transport)

    def call(self, endpoint, log_level=logging.ERROR):
        endpoint_name = endpoint.__class__.__name__

        if not hasattr(self.client.service, endpoint_name):
            raise ValueError(f"Endpoint '{endpoint_name} not found.")
        
        parameters = {key: value for key, value in endpoint.__dict__.items()}

        try:
            response = getattr(self.client.service, endpoint_name)(**parameters)
            return response
        except Exception as e:
            raise Exception(f"Error calling {endpoint_name}: {e}")