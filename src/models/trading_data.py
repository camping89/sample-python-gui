"""Data models for trading information."""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class Account:
    """Account information model."""
    balance: float
    equity: float
    margin_used: float = 0.0
    margin_free: float = 0.0
    drawdown: float = 0.0
    
@dataclass
class Trade:
    """Individual trade model."""
    id: str
    symbol: str
    direction: str  # 'BUY' or 'SELL'
    volume: float
    open_price: float
    current_price: float
    profit: float
    open_time: datetime
    
@dataclass
class Strategy:
    """Trading strategy model."""
    id: str
    name: str
    symbol: str
    timeframe: str
    status: str  # 'ACTIVE', 'INACTIVE', 'PAUSED'
    profit: float = 0.0
    trades_count: int = 0
    
@dataclass
class ProfitData:
    """Profit/loss data for charts."""
    timestamp: datetime
    profit: float
    cumulative_profit: float