"""Data management utilities."""

from datetime import datetime, timedelta
import random
from typing import List
from src.models.trading_data import Account, Trade, Strategy, ProfitData

class DataManager:
    """Manages sample trading data for the application."""
    
    def __init__(self):
        self.account = Account(balance=1215, equity=345, drawdown=0.0)
        self.strategies = self._create_sample_strategies()
        self.profit_history = self._generate_profit_history()
    
    def get_account_info(self) -> Account:
        """Get current account information."""
        return self.account
    
    def get_strategies(self) -> List[Strategy]:
        """Get list of trading strategies."""
        return self.strategies
    
    def get_profit_history(self) -> List[ProfitData]:
        """Get profit history for charts."""
        return self.profit_history
    
    def _create_sample_strategies(self) -> List[Strategy]:
        """Create sample trading strategies."""
        return [
            Strategy(
                id="1",
                name="L_CHANNEL_XAUUSD_M5",
                symbol="XAUUSD",
                timeframe="M5",
                status="ACTIVE",
                profit=12.5,
                trades_count=8
            ),
            Strategy(
                id="2",
                name="L_CHANNEL_BTCUSD_M15",
                symbol="BTCUSD",
                timeframe="M15",
                status="ACTIVE",
                profit=-5.2,
                trades_count=3
            )
        ]
    
    def _generate_profit_history(self) -> List[ProfitData]:
        """Generate sample profit history data."""
        data = []
        base_time = datetime.now() - timedelta(days=7)
        cumulative = 0
        
        for i in range(7):
            profit = random.uniform(-20, 30)
            cumulative += profit
            data.append(ProfitData(
                timestamp=base_time + timedelta(days=i),
                profit=profit,
                cumulative_profit=cumulative
            ))
        
        return data
    
    def update_strategy_status(self, strategy_id: str, status: str):
        """Update strategy status."""
        for strategy in self.strategies:
            if strategy.id == strategy_id:
                strategy.status = status
                break