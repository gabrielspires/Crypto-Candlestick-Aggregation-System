from candlestick_api import CandlestickAPI

if __name__ == "__main__":
    """Calls the methods for fetching and creating/inserting the candlestick data in the
    database.
    Both api methods below use the threading lib to call themselves every .5 seconds. This
    makes sure that the requests are fast enough so that we don't skip seconds and we can
    request data concurrently respecting the limit of 6 requests per second.
    """
    bitcoin_aggregator = CandlestickAPI("USDT_BTC")
    bitcoin_aggregator.fetch_coin_data()
    bitcoin_aggregator.create_candles()

    monero_aggregator = CandlestickAPI("USDT_XMR")
    monero_aggregator.fetch_coin_data()
    monero_aggregator.create_candles()
