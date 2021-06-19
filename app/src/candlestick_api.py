import requests
import json


class CandlestickAPI(object):
    def get_market_data(self, url: str) -> dict:
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
