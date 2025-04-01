# def calculate_moving_average(data, window_size):
#     """Calculate the moving average of a given data series."""
#     return data.rolling(window=window_size).mean()

# def calculate_exponential_moving_average(data, span):
#     """Calculate the exponential moving average of a given data series."""
#     return data.ewm(span=span, adjust=False).mean()

# def calculate_returns(data):
#     """Calculate the returns of a given data series."""
#     return data.pct_change().dropna()

# def calculate_volatility(data, window_size):
#     """Calculate the rolling volatility of a given data series."""
#     return data.rolling(window=window_size).std()

# def normalize_data(data):
#     """Normalize the data to a range of [0, 1]."""
#     return (data - data.min()) / (data.max() - data.min())

# def create_feature_set(data):
#     """Create a feature set from the raw data."""
#     features = pd.DataFrame()
#     features['moving_average'] = calculate_moving_average(data['close'], window_size=20)
#     features['exponential_moving_average'] = calculate_exponential_moving_average(data['close'], span=20)
#     features['returns'] = calculate_returns(data['close'])
#     features['volatility'] = calculate_volatility(data['close'], window_size=20)
#     features['normalized'] = normalize_data(data['close'])
#     return features.dropna()