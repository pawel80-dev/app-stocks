import json
import logging
import os
import azure.functions as func
from shared.api_twelvedata import stock_quote, time_series
from shared.api_ipify import get_public_ip
from shared.calculations import time_series_high_low

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Create the Function App using v2 model
app = func.FunctionApp()


# route: api/stocks?stock=CompanySymbol
# route: api/stocks?user=Username
@app.function_name(name="HttpTrigger-stocks")
@app.route(route="stocks", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC app-stock-exchange.")
    stocks_api_url = "https://api.twelvedata.com"
    api_key = os.getenv("TWELVEDATA_API_KEY")
    stock = req.params.get("stock")
    user = req.params.get("user")
    stocks = []
    low_high_data = []
    stock_list = ["NVDA", "MSFT", "AAPL", "GOOG", "AMZN", "META", "AVGO", "TSLA"]

    if user:
        return f"Ciao {user}, come stai?"
    if stock == "top8" and api_key:
        for stock in stock_list:
            data = json.loads(stock_quote(stocks_api_url, api_key, stock))
            stocks.append(data)
        return json.dumps(stocks)
    if stock == "top8extended" and api_key:
        for stock in stock_list:
        # time_series_data = json.loads(time_series(stocks_api_url, api_key, "MSFT", "1month"))
            time_series_data = time_series(stocks_api_url, api_key, stock, "1month", "2020-01-01", "2026-01-01")
            low_high_data.append(time_series_high_low(json.loads(time_series_data)))
        return json.dumps(low_high_data)
        # data = json.loads(stock_quote(stocks_api_url, api_key, "MSFT"))
        # return f"Company name: {data["name"]}, Price: {data["close"]} {data["currency"]}"
        # data = stock_quote(stocks_api_url, api_key, stock)
        # return data["fifty_two_week"]["high_change"]
    else:
        return "Ciao!"


# route parameter is changed: api/{functionname} to api/message
@app.function_name(name="HttpTrigger-message")
@app.route(route="message", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC API message.")

    # return "Hello, from the stocks API!"
    return json.dumps({"text": "Ciao, from the stocks API!"})


# route parameter is changed: api/{functionname} to api/os
@app.function_name(name="HttpTrigger-env")
@app.route(route="env", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC OS/Environment type.")
    os_type = os.name
    # website_id = os.getenv("WEBSITE_INSTANCE_ID", "local")
    # website_platform = os.getenv("WEBSITE_PLATFORM_VERSION", "unknown")
    az_env = os.getenv("AZURE_ENVIRONMENT", "local")

    return json.dumps({"OS_type": os_type, "Function_Environment": az_env})


# route parameter is changed: api/{functionname} to api/ipcheck
@app.function_name(name="HttpTrigger-ipcheck")
@app.route(route="ipcheck", auth_level=func.AuthLevel.ANONYMOUS)
def ip_check(req: func.HttpRequest) -> str:
    logging.info("AZ-FUNC HttpTrigger-ip-check started.")
    ipify_url = "https://api.ipify.org"
    public_ip = get_public_ip(ipify_url)

    return json.dumps({"public_ip": public_ip})