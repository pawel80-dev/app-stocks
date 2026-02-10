import requests
import logging
import json
import os
import time
from urllib3.exceptions import InsecureRequestWarning

# logger will return the source module name
logger = logging.getLogger(__name__)
# display logging info level
logging.basicConfig(level=logging.INFO)
# Suppress certificate warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def stocks_company(stock_url: str, company_symbol: str, api_key: str) -> str:
    api = f"/query?function=OVERVIEW&symbol={company_symbol}&apikey={api_key}"
    url = stock_url + api
    headers = {
        # "Authorization": f"apikey {api_key}",
        "Content-Type": "application/json"
    }
    response = requests.get(
        url=url,
        headers=headers
    )
    return json.dumps(response.json(), indent=4)
    # if response.status_code == 200:
    #     logger.info("Stocks list successfully retrieved.")
    #     # return response.json()
    #     return json.dumps(response.json(), indent=4)
    # else:
    #     logger.info(f"Failed to retrieved the stocks list: {response.status_code}")
    #     logger.info(response.text)


def daily(stock_url: str, company_symbol: str, api_key: str) -> str:
    api = f"/query?function=TIME_SERIES_DAILY&symbol={company_symbol}&apikey={api_key}"
    url = stock_url + api
    headers = {
        # "Authorization": f"apikey {api_key}",
        "Content-Type": "application/json"
    }
    # payload = {
    #     "country": "pl",
    #     "type": "Common Stock",
    #     "exchange": "GPW",
    #     "symbol": "DNP" # CDR, DNP
    #     }
    response = requests.get(
        url=url,
        headers=headers
        # params=payload
    )
    return json.dumps(response.json(), indent=4)
    # if response.status_code == 200:
    #     logger.info("Stocks list successfully retrieved.")
    #     # return response.json()
    #     return json.dumps(response.json(), indent=4)
    # else:
    #     logger.info(f"Failed to retrieved the stocks list: {response.status_code}")
    #     logger.info(response.text)


# Asynchronous function to make an API request
# async def make_api_request(function, symbol=None, interval=None, series_type=None, **kwargs):
#     url = f"https://www.alphavantage.co/query?function={function}&apikey={API_KEY}"

#     # Add optional parameters
#     if symbol:
#         url += f"&symbol={symbol}"
#     if interval:
#         url += f"&interval={interval}"
#     if series_type:
#         url += f"&series_type={series_type}"
#     for key, value in kwargs.items():
#         url += f"&{key}={value}"

#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         if response.status_code == 200:
#             if response.content:
#                 # Handle CSV responses differently
#                 if response.headers.get('Content-Type') == 'text/csv':
#                     return response.text.splitlines()
#                 else:
#                     return response.json()
#             else:
#                 print(f"Error: Empty response for {url}")
#                 return None
#         else:
#             print(f"Error: {response.status_code} for {url}")
#             return None

    # print("### Sugar ###")
    # sugar_data = await make_api_request("SUGAR", interval="monthly")
    # print(sugar_data)


def main() -> None:
    stocks_api_url = "https://www.alphavantage.co"
    api_key = os.environ["ALPHA_VANTAGE_API_KEY"]
    stock_list = ["IBM", "AAPL", "MSFT", "SONY", "EA", "TTWO", "U"]
    for stock in stock_list:
        data = json.loads(stocks_company(stocks_api_url, stock, api_key))
        print(data)
        # print(f"Data for {stock}: {data["Symbol"]}")
        # time.sleep(1)
    # data_ibm_daily = daily(stocks_api_url, "CDR.WA", api_key)


if __name__ == "__main__":
    main()