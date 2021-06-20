from candlestick_api import CandlestickAPI

if __name__ == "__main__":
    """Calls the methods for fetching and creating/inserting the candlestick data in the
    database.
    Both api methods below use the threading lib to call themselves every .5 seconds. This
    makes sure that the requests are fast enough so that we don't skip seconds and we can
    request data concurrently respecting the limit of 6 requests per second.
    """
    candle_api = CandlestickAPI()

    candle_api.fetch_BTC_data()
    candle_api.fetch_XMR_data()

    candle_api.create_BTC_candles()
    candle_api.create_XMR_candles()
