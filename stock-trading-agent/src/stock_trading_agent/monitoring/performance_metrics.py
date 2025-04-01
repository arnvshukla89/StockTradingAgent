# from typing import List, Dict

# def calculate_sharpe_ratio(returns: List[float], risk_free_rate: float = 0.0) -> float:
#     excess_returns = [r - risk_free_rate for r in returns]
#     return sum(excess_returns) / (len(excess_returns) ** 0.5)

# def calculate_max_drawdown(equity_curve: List[float]) -> float:
#     max_drawdown = 0.0
#     peak = equity_curve[0]
    
#     for value in equity_curve:
#         if value > peak:
#             peak = value
#         drawdown = (peak - value) / peak
#         max_drawdown = max(max_drawdown, drawdown)
    
#     return max_drawdown

# def calculate_performance_metrics(equity_curve: List[float], risk_free_rate: float = 0.0) -> Dict[str, float]:
#     returns = [equity_curve[i] / equity_curve[i - 1] - 1 for i in range(1, len(equity_curve))]
    
#     sharpe_ratio = calculate_sharpe_ratio(returns, risk_free_rate)
#     max_drawdown = calculate_max_drawdown(equity_curve)
    
#     return {
#         "sharpe_ratio": sharpe_ratio,
#         "max_drawdown": max_drawdown
#     }