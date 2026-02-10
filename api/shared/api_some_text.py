import requests
import logging
import json
import os
from urllib3.exceptions import InsecureRequestWarning

# logger will return the source module name
logger = logging.getLogger(__name__)
# display logging info level
logging.basicConfig(level=logging.INFO)
# Suppress certificate warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def get_some_text():
    return "This is some text from the API."


def stock_quote(stock_url: str, api_key: str, symbol: str) -> str:
    api = f"/quote?symbol={symbol}"
    url = stock_url + api
    headers = {
        "Authorization": f"apikey {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=url,
        headers=headers,
        verify=False
    )
    if response.status_code == 200:
        logger.info(f"Stock {symbol} data successfully retrieved.")
        # return json.dumps(response.json(), indent=4)
        return json.dumps(response.json())
    else:
        # logger.info(f"Failed to retrieved {symbol} stock data: {response.json()["code"]}") <-- breaking SWA code!
        logger.info(response.json()["message"])