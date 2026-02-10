import json
import logging
import os
import azure.functions as func
from shared.api_twelvedata import stock_quote

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Create the Function App using v2 model
app = func.FunctionApp()


# route: api/stocks?stock=CompanySymbol
# route: api/stocks?user=Username
# https://functionAppName.azurewebsites.net/api/stocks?stock=CompanySymbol
# https://functionAppName.azurewebsites.net/api/stocks?user=YourName
@app.function_name(name="HttpTrigger-stocks")
@app.route(route="stocks", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC app-stock-exchange.")
    stocks_api_url = "https://api.twelvedata.com"
    api_key = os.getenv("TWELVEDATA_API_KEY")
    stock = req.params.get("stock")
    user = req.params.get("user")
    stocks = []
    stock_list = ["NVDA", "MSFT", "AAPL", "GOOG", "AMZN", "META", "AVGO", "TSLA"]

    if user:
        return f"Ciao {user}, come stai?"
    if stock == "top8" and api_key:
        for stock in stock_list:
            data = json.loads(stock_quote(stocks_api_url, api_key, stock))
            stocks.append(data)
        # data = json.loads(stock_quote(stocks_api_url, api_key, "MSFT"))
        # return f"Company name: {data["name"]}, Price: {data["close"]} {data["currency"]}"
        # data = stock_quote(stocks_api_url, api_key, stock)
        # return data["fifty_two_week"]["high_change"]
        return json.dumps(stocks, indent=4)
    else:
        return "Ciao!"


# route parameter is changed: api/{functionname} to api/message
@app.function_name(name="HttpTrigger-api")
@app.route(route="message", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC API message.")

    # return "Hello, from the stocks API!"
    return json.dumps({"text": "Ciao, from the stocks API!"})


# route parameter is changed: api/{functionname} to api/os
@app.function_name(name="HttpTrigger-api-env")
@app.route(route="env", auth_level=func.AuthLevel.ANONYMOUS)
def get_basic(req: func.HttpRequest) -> str:
    logger.info("AZ-FUNC OS/Environment type.")
    os_type = os.name
    # website_id = os.getenv("WEBSITE_INSTANCE_ID", "local")
    # website_platform = os.getenv("WEBSITE_PLATFORM_VERSION", "unknown")
    az_env = os.getenv("AZURE_ENVIRONMENT", "local")

    return json.dumps({"OS_type": os_type, "Function_Environment": az_env})