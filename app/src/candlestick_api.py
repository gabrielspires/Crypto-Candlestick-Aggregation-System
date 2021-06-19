import requests
import json
from typing import Union
from datetime import datetime


class CandlestickAPI(object):
    def __init__(self):
        self.bitcoin_values = {}
        self.monero_values = {}

    def get_market_data(self, url: str) -> Union[dict, None]:
        """Sends a request for the market data of all currency pairs in the exchange.

        Args:
            url (str): The url of the Poloniex API with the apropriate command.

        Returns:
            dict: JSON response with the execution price of the most recent trade for all
            currency pairs.
        """

        response = requests.get(url)

        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def extract_coin_info(self, currency_pair: str) -> Union[dict, None]:
        """Extracts the last value of the currency pair we want from the api's response and
        return it with the date and time as the key.

        Args:
            currency_pair (str): One of the pairs listed at
            https://docs.poloniex.com/?shell#currency-pair-ids

        Returns:
            Union[dict, None]: Returns a dictionary with the currency pair as a key with it's value
            as the execution price of the most recent trade for that pair. If the request fails it
            returns None.
        """

        api_command = "returnTicker"
        api_url = "https://poloniex.com/public?command=" + api_command

        request_answer = None
        datetime_now = None

        try:
            datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            request_answer = self.get_market_data(api_url)
        except Exception as e:
            print("Error with url %s : %s" % (api_url, e))

        if request_answer is not None:
            response = {datetime_now: float(request_answer[currency_pair]["last"])}
            return response
        else:
            return None

    def request_BTC_data(self):
        crypto_data = self.extract_coin_info("USDT_BTC")

        if crypto_data is None:
            print("Request failed")

        self.bitcoin_values.update(crypto_data)

    def request_XMR_data(self):
        crypto_data = self.extract_coin_info("USDT_XMR")
        if crypto_data is None:
            print("Request failed")

        self.monero_values.update(crypto_data)
