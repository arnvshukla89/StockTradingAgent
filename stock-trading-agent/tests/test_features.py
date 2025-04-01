# import pytest
# from src.trading_agent.feature_engineering.features import some_feature_function
# from src.trading_agent.feature_engineering.ta_features import calculate_macd
# from src.trading_agent.feature_engineering.fundamental_features import extract_fundamental_features

# def test_some_feature_function():
#     # Test case for some_feature_function
#     input_data = [1, 2, 3, 4, 5]
#     expected_output = [1, 4, 9, 16, 25]  # Example expected output
#     assert some_feature_function(input_data) == expected_output

# def test_calculate_macd():
#     # Test case for MACD calculation
#     prices = [1, 2, 3, 4, 5]
#     expected_macd = ...  # Define expected MACD output
#     assert calculate_macd(prices) == expected_macd

# def test_extract_fundamental_features():
#     # Test case for extracting fundamental features
#     raw_data = {'revenue': 100, 'profit': 20}
#     expected_features = {'profit_margin': 0.2}  # Example expected output
#     assert extract_fundamental_features(raw_data) == expected_features