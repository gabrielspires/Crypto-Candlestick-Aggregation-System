import time
import threading
import requests
import json
import pandas as pd
from typing import Union
from datetime import datetime

from candlestick_aggregator.database import Database


class CandlestickAPI(object):
    def __init__(self):
        self.bitcoin_values = {}
        self.monero_values = {}

        self.db = Database()
        self.sem = threading.Semaphore()

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
            currency_pair (str): Name of the currency pair ('USDT_BTC' or 'USDT_XMR')

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

    def fetch_BTC_data(self):
        """Request the bitcoin data from the extract_coin_info method and
        append the data to the bitcoin_values dictionary.
        """
        threading.Timer(0.3, self.fetch_BTC_data).start()
        print("Sending USDT_BTC request at", datetime.now())
        crypto_data = self.extract_coin_info("USDT_BTC")

        if crypto_data is None:
            print("Request failed")

        self.bitcoin_values.update(crypto_data)

    def fetch_XMR_data(self):
        """Request the monero data from the extract_coin_info method and
        append the data to the monero_values dictionary.
        """
        threading.Timer(0.3, self.fetch_XMR_data).start()
        print("Sending USDT_XMR request at", datetime.now())
        crypto_data = self.extract_coin_info("USDT_XMR")
        if crypto_data is None:
            print("Request failed")

        self.monero_values.update(crypto_data)

    def aggregate_coin_data(self, coin_values: dict, period: str) -> pd.DataFrame:
        """Transforms the coin dictionaries into a pandas dataframe and use the resample
        method to aggregate the values into candles (ohlc).

        Args:
            coin_values (dict): dictionary to serve as data for the dataframe creation that contains
            the datatime and value of the trades.
            period (str): Period of the candle in minutes ('1min', '5min' or '15min').

        Returns:
            pd.DataFrame: Returns the pandas dataframe with the candles.
        """

        df = pd.DataFrame.from_dict(coin_values, orient="index", columns=["last_price"])
        df.index = pd.to_datetime(df.index)

        ohlc_candles = df["last_price"].resample(period).ohlc()

        return ohlc_candles

    def fetch_last_candle(self, currency_pair: str, period: str, coin_values: dict) -> dict:
        """Grabs the last candle created for the period and returns it in a dictionary
        that also contains the currency pair name.

        Args:
            currency_pair (str): Name of the currency pair ('USDT_BTC' or 'USDT_XMR').
            period (str): Period of the candle in minutes ('1min', '5min' or '15min').
            coin_values (dict): Dictionary with the data and values of the trades.

        Returns:
            dict: Dictionary withh the ohlc data of the period and currency pair
        """
        ohlc_df = self.aggregate_coin_data(coin_values, period)

        timestamp = ohlc_df.index[-1].to_pydatetime()
        candle_values = ohlc_df.iloc[-1].to_dict()

        last_candle_info = {}
        last_candle_info["currency_pair"] = currency_pair
        last_candle_info["period"] = period
        last_candle_info["date"] = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        last_candle_info.update(candle_values)

        return last_candle_info

    def create_BTC_candles(self):
        """Constantly checks if it's the right time to generate a candle and insert it in the DB.
        Only saves the data at the right time for the period.
        """
        current_time = time.time()
        wait = False
        currency_pair = "USDT_BTC"

        if int(current_time) % (60) == 59:
            print("Generating 1min candle for USDT_BTC...")
            period = "1min"
            self.sem.acquire()

            last_1min_candle = self.fetch_last_candle(currency_pair, period, self.bitcoin_values)
            self.db.insert(last_1min_candle)

            self.sem.release()
            wait = True
        if int(time.time()) % (5 * 60) == (5 * 60 - 1):
            print("Generating 5min candle for USDT_BTC...")
            period = "5min"
            self.sem.acquire()

            last_5min_candle = self.fetch_last_candle(currency_pair, period, self.bitcoin_values)
            self.db.insert(last_5min_candle)

            self.sem.release()
            wait = True
        if int(time.time()) % (15 * 60) == (15 * 60 - 1):
            print("Generating 15min candle for USDT_BTC...")
            period = "15min"
            self.sem.acquire()

            last_15min_candle = self.fetch_last_candle(currency_pair, period, self.bitcoin_values)
            self.db.insert(last_15min_candle)

            self.sem.release()
            wait = True

            self.bitcoin_values.clear()

        if wait is True:
            time.sleep(1)

        threading.Timer(0.5, self.create_BTC_candles).start()

    def create_XMR_candles(self):
        """Constantly checks if it's the right time to generate a candle and insert it in the DB.
        Only saves the data at the right time for the period.
        """
        current_time = time.time()
        wait = False
        currency_pair = "USDT_XMR"

        if int(current_time) % (60) == 59:
            print("Generating 1min candle for USDT_XMR...")
            period = "1min"
            self.sem.acquire()

            last_1min_candle = self.fetch_last_candle(currency_pair, period, self.monero_values)
            self.db.insert(last_1min_candle)

            self.sem.release()
            wait = True
        if int(time.time()) % (5 * 60) == (5 * 60 - 1):
            print("Generating 5min candle for USDT_XMR...")
            period = "5min"
            self.sem.acquire()

            last_5min_candle = self.fetch_last_candle(currency_pair, period, self.monero_values)
            self.db.insert(last_5min_candle)

            self.sem.release()
            wait = True
        if int(time.time()) % (15 * 60) == (15 * 60 - 1):
            print("Generating 15min candle for USDT_XMR...")
            period = "15min"
            self.sem.acquire()

            last_15min_candle = self.fetch_last_candle(currency_pair, period, self.monero_values)
            self.db.insert(last_15min_candle)

            self.sem.release()
            wait = True

            self.monero_values.clear()

        if wait is True:
            time.sleep(1)

        threading.Timer(0.5, self.create_XMR_candles).start()
