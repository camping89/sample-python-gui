"""Configuration settings for the trading GUI application."""

# Application settings
APP_TITLE = "SEN TRADING SYSTEM"
APP_VERSION = "1.0.0"
WINDOW_SIZE = "1200x800"
MIN_WINDOW_SIZE = (800, 600)

# Color scheme
COLORS = {
    'bg_primary': '#f0f0f0',
    'bg_secondary': '#e8e8e8', 
    'accent': '#20b2aa',
    'text_primary': '#333333',
    'text_secondary': '#666666',
    'success': '#4caf50',
    'warning': '#ff9800',
    'error': '#f44336'
}

# Trading settings
DEFAULT_BALANCE = 1215
DEFAULT_EQUITY = 345
MAX_TRADES = 5
MAX_LOSS_PERCENT = 3

# Chart settings
CHART_UPDATE_INTERVAL = 1000  # milliseconds
DEFAULT_TIMEFRAME = "M5"