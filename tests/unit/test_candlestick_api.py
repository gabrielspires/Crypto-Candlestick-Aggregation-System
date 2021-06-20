from candlestick_aggregator.candlestick_api import CandlestickAPI
import json
from datetime import datetime
from unittest.mock import patch, Mock
from freezegun import freeze_time


@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_get_market_data(mock_get, mock_db):
    mock_get.return_value.content = '{"USDT_BTC": {}}'

    api = CandlestickAPI()
    valid_url = "test_url"
    response = api.get_market_data(valid_url)

    assert "USDT_BTC" in response


@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_get_market_data_invalid_command(mock_get, mock_db):
    error_response = '{"error": "Invalid command."}'

    mock_get.return_value.content = error_response

    api = CandlestickAPI()
    invalid_command = "test_url"
    assert api.get_market_data(invalid_command) == json.loads(error_response)


@freeze_time("2021-01-01 00:00:00")
@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_extract_coin_info(mock_get, mock_db):
    mock_get.return_value.content = '{"test_pair": {"last": 0.0}}'

    api = CandlestickAPI()
    currency_pair = "test_pair"
    response = api.extract_coin_info(currency_pair)
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    assert response == {datetime_now: float(0.0)}


@freeze_time("2021-01-01 00:00:00")
@patch("candlestick_aggregator.candlestick_api.threading")
@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_fetch_BTC_data(mock_get, mock_db, mock_threading):
    mock_get.return_value.content = '{"USDT_BTC": {"last": 0.0}}'

    api = CandlestickAPI()
    api.fetch_BTC_data()
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    assert datetime_now in api.bitcoin_values


@freeze_time("2021-01-01 00:00:00")
@patch("candlestick_aggregator.candlestick_api.threading")
@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_fetch_XMR_data(mock_get, mock_db, mock_threading):
    mock_get.return_value.content = '{"USDT_XMR": {"last": 0.0}}'

    api = CandlestickAPI()
    api.fetch_XMR_data()
    datetime_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    assert datetime_now in api.monero_values


@patch("candlestick_aggregator.candlestick_api.Database")
def test_aggregate_coin_data(mock_db):
    test_currency_pair = "TEST_COIN"
    test_period = "1min"
    test_coin_values = {
        "2021-01-01 00:00:00": 80,
        "2021-01-01 00:00:30": 120,
        "2021-01-01 00:00:45": 50,
        "2021-01-01 00:00:59": 70,
    }

    api = CandlestickAPI()
    method_return = api.fetch_last_candle(test_currency_pair, test_period, test_coin_values)

    expected_result = {
        "currency_pair": test_currency_pair,
        "period": test_period,
        "date": "2021-01-01 00:00:00",
        "open": 80,
        "high": 120,
        "low": 50,
        "close": 70,
    }

    assert method_return == expected_result


# def test_fetch_last_candle():
#     assert True


@freeze_time("2021-01-01 00:00:59")
@patch("candlestick_aggregator.candlestick_api.threading")
@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_create_BTC_candles_1min(mock_get, mock_db, mock_threading):
    api = CandlestickAPI()
    api.db.insert = Mock()
    api.fetch_last_candle = Mock()

    candle_1min = {
        "currency_pair": "TEST_PAIR",
        "period": "1min",
        "date": "2021-01-01 00:00:00",
        "open": 10.2,
        "high": 12.5,
        "low": 8.5,
        "close": 9.1,
    }
    api.fetch_last_candle.return_value = candle_1min

    api.create_BTC_candles()

    api.db.insert.assert_called_with(candle_1min)


@freeze_time("2021-01-01 00:04:59")
@patch("candlestick_aggregator.candlestick_api.threading")
@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_create_BTC_candles_5min(mock_get, mock_db, mock_threading):
    api = CandlestickAPI()
    api.db.insert = Mock()
    api.fetch_last_candle = Mock()

    candle_5min = {
        "currency_pair": "TEST_PAIR",
        "period": "5min",
        "date": "2021-01-01 00:00:00",
        "open": 10.2,
        "high": 12.5,
        "low": 8.5,
        "close": 9.1,
    }
    api.fetch_last_candle.return_value = candle_5min

    api.create_BTC_candles()

    api.db.insert.assert_called_with(candle_5min)


@freeze_time("2021-01-01 00:14:59")
@patch("candlestick_aggregator.candlestick_api.threading")
@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_create_BTC_candles_15min(mock_get, mock_db, mock_threading):
    api = CandlestickAPI()
    api.db.insert = Mock()
    api.fetch_last_candle = Mock()

    candle_15min = {
        "currency_pair": "TEST_PAIR",
        "period": "15min",
        "date": "2021-01-01 00:00:00",
        "open": 10.2,
        "high": 12.5,
        "low": 8.5,
        "close": 9.1,
    }
    api.fetch_last_candle.return_value = candle_15min

    api.create_BTC_candles()

    api.db.insert.assert_called_with(candle_15min)


@freeze_time("2021-01-01 00:00:59")
@patch("candlestick_aggregator.candlestick_api.threading")
@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_create_XMR_candles_1min(mock_get, mock_db, mock_threading):
    api = CandlestickAPI()
    api.db.insert = Mock()
    api.fetch_last_candle = Mock()

    candle_1min = {
        "currency_pair": "TEST_PAIR",
        "period": "1min",
        "date": "2021-01-01 00:00:00",
        "open": 10.2,
        "high": 12.5,
        "low": 8.5,
        "close": 9.1,
    }
    api.fetch_last_candle.return_value = candle_1min

    api.create_XMR_candles()

    api.db.insert.assert_called_with(candle_1min)


@freeze_time("2021-01-01 00:04:59")
@patch("candlestick_aggregator.candlestick_api.threading")
@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_create_XMR_candles_5min(mock_get, mock_db, mock_threading):
    api = CandlestickAPI()
    api.db.insert = Mock()
    api.fetch_last_candle = Mock()

    candle_5min = {
        "currency_pair": "TEST_PAIR",
        "period": "1min",
        "date": "2021-01-01 00:00:00",
        "open": 10.2,
        "high": 12.5,
        "low": 8.5,
        "close": 9.1,
    }
    api.fetch_last_candle.return_value = candle_5min

    api.create_XMR_candles()

    api.db.insert.assert_called_with(candle_5min)


@freeze_time("2021-01-01 00:14:59")
@patch("candlestick_aggregator.candlestick_api.threading")
@patch("candlestick_aggregator.candlestick_api.Database")
@patch("candlestick_aggregator.candlestick_api.requests.get")
def test_create_XMR_candles_15min(mock_get, mock_db, mock_threading):
    api = CandlestickAPI()
    api.db.insert = Mock()
    api.fetch_last_candle = Mock()

    candle_15min = {
        "currency_pair": "TEST_PAIR",
        "period": "1min",
        "date": "2021-01-01 00:00:00",
        "open": 10.2,
        "high": 12.5,
        "low": 8.5,
        "close": 9.1,
    }
    api.fetch_last_candle.return_value = candle_15min

    api.create_XMR_candles()

    api.db.insert.assert_called_with(candle_15min)
