import pandas as pd
import time
from polygon import RESTClient
from polygon.exceptions import ResponseError

class HistoricalData:
    def __init__(self, symbol: str, start_date: str, end_date: str):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    def fetch_data(self, max_retries=5, wait_time=5):
        client = RESTClient("pvS1MZH8asaRyx71YaK1EHNi7yDaXQ6y")
        aggs = []
        
        for attempt in range(max_retries):
            try:
                for a in client.list_aggs(
                    self.symbol,
                    1,
                    "day",
                    self.start_date,
                    self.end_date,
                    adjusted=True,
                    sort="asc",
                ):
                    aggs.append(a)
                return {"results": aggs}  # Return data if successful
            except ResponseError as e:
                if e.response.status_code == 429:  # If rate-limited (429)
                    print(f"Rate limit hit for {self.symbol}. Retrying in {wait_time} seconds...")
                    time.sleep(wait_time)  # Wait for the specified time
                    wait_time *= 2  # Exponential backoff (double the wait time)
                else:
                    print(f"Error fetching data for {self.symbol}: {e}")
                    break  # Exit on any other error (non-rate-limiting)
        return {"results": []}  # Return empty data if retries are exhausted

    def process_data(self, data):
        df = pd.DataFrame(data['results'])
        if 't' in df.columns:
            df['t'] = pd.to_datetime(df['t'], unit='ms')
            df.set_index('t', inplace=True)
        df.rename(columns={
            'o': 'open',
            'h': 'high',
            'l': 'low',
            'c': 'close',
            'v': 'volume',
            'vw': 'vwap',
            'n': 'trades'
        }, inplace=True)
        df['ticker'] = self.symbol
        return df

    def get_historical_data(self):
        raw_data = self.fetch_data()
        if raw_data['results']:
            processed_data = self.process_data(raw_data)
            return processed_data
        else:
            print(f"No data found for {self.symbol}.")
            return pd.DataFrame()  # Return an empty DataFrame if no data is fetched
