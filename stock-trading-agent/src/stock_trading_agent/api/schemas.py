# from pydantic import BaseModel
# from typing import List, Optional

# class TradeRequest(BaseModel):
#     symbol: str
#     quantity: int
#     order_type: str  # e.g., 'buy' or 'sell'
#     price: Optional[float] = None  # Optional for market orders

# class TradeResponse(BaseModel):
#     trade_id: str
#     status: str  # e.g., 'success' or 'failed'
#     message: Optional[str] = None

# class HistoricalDataRequest(BaseModel):
#     symbol: str
#     start_date: str  # Format: YYYY-MM-DD
#     end_date: str    # Format: YYYY-MM-DD

# class HistoricalDataResponse(BaseModel):
#     symbol: str
#     data: List[dict]  # List of historical data points

# class InferenceRequest(BaseModel):
#     features: List[float]  # List of feature values for prediction

# class InferenceResponse(BaseModel):
#     prediction: float  # Predicted value
#     confidence: float   # Confidence level of the prediction