"""Main entry point for the SEN Trading System GUI application."""

import tkinter as tk
from tkinter import ttk
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.app import TradingApp

def main():
    """Initialize and run the trading application."""
    root = tk.Tk()
    app = TradingApp(root)
    app.run()

if __name__ == "__main__":
    main()