# SEN Trading System GUI

A Python-based trading system GUI application built with tkinter, designed for managing trading strategies and monitoring account performance.

## Features

- **Main Dashboard**: Real-time account monitoring with balance, equity, and profit/loss charts
- **Strategy Manager**: Add, remove, and control trading strategies
- **Settings Panel**: Configure trading parameters, connection settings, and display options
- **Multi-screen Navigation**: Easy switching between different application screens

## Project Structure

```
sample-python-gui/
├── main.py                 # Application entry point
├── run.py                  # Alternative launcher
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── doc/
│   └── gui.png            # Reference GUI design
└── src/
    ├── app.py             # Main application class
    ├── components/        # Reusable UI components
    │   └── widgets.py     # Custom widgets
    ├── screens/           # Application screens
    │   ├── main_screen.py      # Main dashboard
    │   ├── strategy_screen.py  # Strategy management
    │   └── settings_screen.py  # Settings panel
    ├── models/            # Data models
    │   └── trading_data.py     # Trading data structures
    └── utils/             # Utilities
        └── data_manager.py     # Data management
```

## Installation

1. Ensure Python 3.7+ is installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

```bash
# Option 1: Direct execution
python main.py

# Option 2: Using the run script
python run.py
```

## Navigation

- **File Menu**: Exit application
- **View Menu**: Switch between screens
  - Main Dashboard: Account overview and charts
  - Strategy Manager: Manage trading strategies
  - Settings: Configure application settings

## Configuration

Edit `config.py` to customize:
- Application appearance (colors, window size)
- Trading parameters (max trades, max loss)
- Chart update intervals
- Default values

## Sample Data

The application includes sample data generators for demonstration:
- Mock account information
- Sample trading strategies
- Generated profit/loss history

## Future Enhancements

This is a foundational structure that can be extended with:
- Real MT5/trading platform integration
- Database persistence
- Advanced charting with additional indicators
- Real-time data feeds
- Strategy backtesting capabilities
- Export/import functionality# Default branch update
