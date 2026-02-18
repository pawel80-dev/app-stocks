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


# All responses return JSON format by default unless otherwise specified.
def stocks_list(stock_url: str, api_key: str) -> str:
    api = "/stocks"
    url = stock_url + api
    headers = {
        "Authorization": f"apikey {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "country": "pl",
        "type": "Common Stock",
        "exchange": "GPW",
        "symbol": "DNP" # CDR, DNP
        }
    response = requests.get(
        url=url,
        headers=headers,
        params=payload
    )
    if response.status_code == 200:
        logger.info("Stocks list successfully retrieved.")
        # return response.json()
        return json.dumps(response.json(), indent=4)
    else:
        logger.info(f"Failed to retrieved the stocks list: {response.status_code}")
        logger.info(response.text)


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
    # if response.json()["code"] == 200:
    if response.status_code == 200:
        logger.info(f"Stock {symbol} data successfully retrieved.")
        # return json.dumps(response.json(), indent=4)
        return json.dumps(response.json())
    else:
        # logger.info(f"Failed to retrieved {symbol} stock data: {response.json()["code"]}")   <-- breaking SWA code!
        logger.info(response.json()["message"])


def stock_price(stock_url: str, api_key: str, symbol: str) -> str:
    api = f"/price?symbol={symbol}"
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
        logger.info(f"Stock {symbol} latest price successfully retrieved.")
        # return json.dumps(response.json(), indent=4)
        return json.dumps(response.json())
    else:
        # logger.info(f"Failed to retrieved {symbol} stock price: {response.json()["code"]}")   <-- breaking SWA code!
        logger.info(response.json()["message"])


def time_series(stock_url: str, api_key: str, symbol: str, interval: str, start_date: str, end_date: str) -> str:
    api = f"/time_series?symbol={symbol}&interval={interval}&start_date={start_date}&end_date={end_date}"
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
    # if response.json()["code"] == 200:
    if response.status_code == 200:
        logger.info(f"Time series data for {symbol} successfully retrieved.")
        return json.dumps(response.json(), indent=4)
    else:
        # logger.info(f"Failed to retrieved time series data for {symbol}: {response.json()["code"]}")   <-- breaking SWA code!
        logger.info(response.json()["message"])


# TODO:
# API calls error - how to solve 200, 400 issue?

def main() -> None:
    stocks_api_url = "https://api.twelvedata.com"
    api_key =os.getenv("TWELVEDATA_API_KEY", "local")
    stock_list = ["NVDA", "MSFT", "AAPL", "GOOG", "AMZN", "META", "AVGO", "TSLA"]
    for stock in stock_list:
        data = json.loads(stock_quote(stocks_api_url, api_key, stock))
        print(data)
    # stock_price_data = stock_price(stocks_api_url, api_key, "MSFT")
    # data = json.loads(stock_quote(stocks_api_url, api_key, "MSFT"))
    # print(data)
    # print(stock_price_data)
    # print(f"Company name: {data["name"]}, Price: {data["close"]} {data["currency"]}")
    # time_series_data = json.loads(time_series(stocks_api_url, api_key, "MSFT", "1month"))
    # time_series_data = time_series(stocks_api_url, api_key, "MSFT", "1month", "2020-01-01", "2026-01-01")
    # print(time_series_data)


if __name__ == "__main__":
    main()