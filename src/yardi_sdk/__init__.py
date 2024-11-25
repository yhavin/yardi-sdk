from dotenv import load_dotenv
load_dotenv()
from .core import Client, Response
from . import endpoints
from .utils import type_map