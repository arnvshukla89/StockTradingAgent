import pandas as pd
from stock_trading_agent.enums.ticker import Tickers
from stock_trading_agent.data_ingestion.historical_data import HistoricalData
import os
import time
from polygon.exceptions import ResponseError

# Define start and end dates
start_date = "2023-03-21"
end_date = "2025-03-21"

# List to store data for all tickers
all_data = []

# Retry logic for fetching data with rate-limit handling
def fetch_data_with_retry(ticker, max_retries=5, wait_time=5):
    """Fetch historical data for a ticker with exponential backoff in case of rate-limit errors."""
    for attempt in range(max_retries):
        try:
            # Initialize HistoricalData object
            historical_data = HistoricalData(ticker.value, start_date, end_date)
            # Fetch the data
            data = historical_data.get_historical_data()
            return data
        except ResponseError as e:
            if e.response.status_code == 429:  # Handle 429: Too Many Requests (rate limit)
                print(f"Rate limit hit for {ticker.value}. Retrying in {wait_time} seconds...")
                time.sleep(wait_time)  # Wait before retrying
                wait_time *= 2  # Exponential backoff (double the wait time)
            else:
                print(f"Unexpected error while fetching data for {ticker.value}: {e}")
                break  # Break if it's not a rate limit issue
    print(f"Max retries reached for {ticker.value}. Skipping.")
    return None  # Return None if max retries are reached

# Loop through all tickers and fetch data
for ticker in Tickers:
    print(f"Fetching data for {ticker.value}")
    data = fetch_data_with_retry(ticker)
    
    if data is not None:
        all_data.append(data)
    else:
        print(f"Skipping {ticker.value} due to failure to fetch data.")

# Combine all data into a single DataFrame
if all_data:
    combined_data = pd.concat(all_data)
else:
    print("No data was fetched. Exiting.")
    exit()

# Save the combined data to a Parquet file
file_path = os.path.join(os.path.dirname(__file__), "../../data/raw/all_tickers_data.parquet")
combined_data.to_parquet(file_path, compression='snappy')

print(f"Data saved to {file_path}")
