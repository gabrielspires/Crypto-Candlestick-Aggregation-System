from src.candlestick_api import CandlestickAPI
import json
from unittest.mock import patch  # , Mock


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
