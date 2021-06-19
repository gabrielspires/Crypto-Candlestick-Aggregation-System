from src.candlestick_api import CandlestickAPI
import json
from datetime import datetime
from unittest.mock import patch  # , Mock
from freezegun import freeze_time


@patch("src.candlestick_api.requests.get")
def test_get_market_data(mock_get):
    mock_get.return_value.content = '{"USDT_BTC": {}}'

    api = CandlestickAPI()
    valid_url = "test_url"
    response = api.get_market_data(valid_url)

    assert "USDT_BTC" in response


@patch("src.candlestick_api.requests.get")
def test_get_market_data_invalid_command(mock_get):
    error_response = '{"error": "Invalid command."}'

    mock_get.return_value.content = error_response

    api = CandlestickAPI()
    invalid_command = "test_url"
    assert api.get_market_data(invalid_command) == json.loads(error_response)


@freeze_time("2021-01-01 00:00:00")
@patch("src.candlestick_api.requests.get")
def test_extract_coin_info(mock_get):
    mock_get.return_value.content = '{"test_pair": {"last": 0.0}}'

    api = CandlestickAPI()
    currency_pair = "test_pair"
    response = api.extract_coin_info(currency_pair)
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    assert response == {datetime_now: float(0.0)}


@freeze_time("2021-01-01 00:00:00")
@patch("src.candlestick_api.requests.get")
def test_request_BTC_data(mock_get):
    mock_get.return_value.content = '{"USDT_BTC": {"last": 0.0}}'

    api = CandlestickAPI()
    api.request_BTC_data()
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    assert datetime_now in api.bitcoin_values


@freeze_time("2021-01-01 00:00:00")
@patch("src.candlestick_api.requests.get")
def test_request_XMR_data(mock_get):
    mock_get.return_value.content = '{"USDT_XMR": {"last": 0.0}}'

    api = CandlestickAPI()
    api.request_XMR_data()
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    assert datetime_now in api.monero_values
