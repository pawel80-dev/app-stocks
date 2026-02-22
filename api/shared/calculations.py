import logging
import os
import json

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

msn_dict = {
"meta": {
"symbol": "MSFT",
"interval": "1month",
"currency": "USD",
"exchange_timezone": "America/New_York",
"exchange": "NASDAQ",
"mic_code": "XNGS",
"type": "Common Stock"
},
"values": [
{
"datetime": "2025-09-01",
"open": "500.47000",
"high": "519.29999",
"low": "492.37000",
"close": "517.95001",
"volume": "424025500"
},
{
"datetime": "2025-08-01",
"open": "535",
"high": "538.25",
"low": "498.51001",
"close": "506.69000",
"volume": "454888500"
},
{
"datetime": "2025-07-01",
"open": "496.47000",
"high": "555.45001",
"low": "488.70001",
"close": "533.5",
"volume": "396881900"
},
{
"datetime": "2025-04-01",
"open": "374.64999",
"high": "396.66000",
"low": "344.79001",
"close": "395.26001",
"volume": "562967600"
},
{
"datetime": "2024-11-01",
"open": "409.010010",
"high": "429.32999",
"low": "405.57001",
"close": "423.45999",
"volume": "442321200"
},
{
"datetime": "2024-10-01",
"open": "428.45001",
"high": "438.5",
"low": "406.29999",
"close": "406.35001",
"volume": "440745500"
},
{
"datetime": "2024-09-01",
"open": "417.91000",
"high": "441.85001",
"low": "400.79999",
"close": "430.29999",
"volume": "376921200"
},
{
"datetime": "2020-07-01",
"open": "203.14000",
"high": "216.38000",
"low": "197.50999",
"close": "205.0099945",
"volume": "770190800"
},
{
"datetime": "2020-06-01",
"open": "182.53999",
"high": "204.39999",
"low": "181.35001",
"close": "203.50999",
"volume": "764965400"
},
{
"datetime": "2020-05-01",
"open": "175.80000",
"high": "187.50999",
"low": "173.80000",
"close": "183.25",
"volume": "688845000"
}
],
"status": "ok"
}

def time_series_high_low(data: dict) -> dict:
    if "values" in data and isinstance(data["values"], list) and len(data["values"]) > 0:
        high = max(float(entry["high"]) for entry in data["values"])
        low = min(float(entry["low"]) for entry in data["values"])
        return {"symbol": data["meta"]["symbol"], "highest": f"{high:.2f}", "lowest": f"{low:.2f}"}
    else:
        logger.info("Invalid data format for time series high/low calculation.")
        return {"symbol": data["meta"]["symbol"], "highest": None, "lowest": None}


def main() -> None:
    stocks_api_url = "https://api.twelvedata.com"
    api_key =os.getenv("TWELVEDATA_API_KEY", "local")
    stock_list = ["NVDA", "MSFT", "AAPL", "GOOG", "AMZN", "META", "AVGO", "TSLA"]
    time_series_high_low_data = time_series_high_low(msn_dict)
    print(time_series_high_low_data)


if __name__ == "__main__":
    main()

