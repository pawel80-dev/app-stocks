import requests
from urllib3.exceptions import InsecureRequestWarning
import logging
import json
import os

# logger will return the source module name
logger = logging.getLogger(__name__)
# display logging info level
logging.basicConfig(level=logging.INFO)
# Suppress certificate warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def get_some_text():
    return "This is some text from the API."
