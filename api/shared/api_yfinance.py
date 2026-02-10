import yfinance as yf
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_stock(symbol: str) -> dict:
    try:
        stock = yf.Ticker(symbol)
        # historical_data = stock.history(start="2026-01-01", end="2026-01-23", interval="1d")
        # historical_data = stock.history(period="1mo")
        # return historical_data
        # return historical_data[['Open', 'High', 'Low', 'Close', 'Volume']]
        return {
            "symbol": symbol,
            "company_name": stock.info.get("longName"),
            "price": stock.info.get("currentPrice"),
            "currency": stock.info.get("currency"),
            # "recommendations": stock.get_recommendations()
            }

    except Exception as e:
        logger.info(f"Generic error when fetching the data for {symbol}: {e}")
        return None


def main() -> None:
    stocks_games = ["MSFT", "SONY", "EA", "TTWO", "U", "UBI.PA"]
    stocks_pl = ["PKN.WA", "PKO.WA", "KGH.WA", "PZU.WA", "SPL.WA", "PEO.WA", "MBK.WA",
              "DNP.WA", "LPP.WA", "ALE.WA", "CDR.WA", "PGE.WA", "ZAB.WA", "BDX.WA",
              "PCO.WA", "ALR.WA", "OPL.WA", "KTY.WA", "KRU.WA", "CCC.WA"]
    for symbol in stocks_games:
        data = get_stock(symbol)
        print(data)


if __name__ == "__main__":
    main()