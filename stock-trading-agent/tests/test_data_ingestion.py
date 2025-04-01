# import pytest
# from src.trading_agent.data_ingestion.historical_data import fetch_historical_data
# from src.trading_agent.data_ingestion.real_time_stream import RealTimeStream
# from src.trading_agent.data_ingestion.preprocess import preprocess_data

# def test_fetch_historical_data():
#     # Test fetching historical data from the API
#     data = fetch_historical_data('AAPL', '2023-01-01', '2023-01-31')
#     assert data is not None
#     assert isinstance(data, list)
#     assert len(data) > 0

# def test_real_time_stream_initialization():
#     # Test initialization of the real-time stream
#     stream = RealTimeStream('AAPL')
#     assert stream.symbol == 'AAPL'
#     assert stream.is_connected() is True

# def test_preprocess_data():
#     # Test data preprocessing
#     raw_data = [{'price': 100, 'volume': 10}, {'price': 101, 'volume': 15}]
#     processed_data = preprocess_data(raw_data)
#     assert processed_data is not None
#     assert isinstance(processed_data, list)
#     assert all('price' in entry for entry in processed_data)
#     assert all('volume' in entry for entry in processed_data)