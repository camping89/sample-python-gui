"""Main dashboard screen for the trading application."""

import tkinter as tk
from tkinter import ttk
import config
from src.components.widgets import StatCard, ProfitChart, StrategyList
from src.utils.data_manager import DataManager

class MainScreen(tk.Frame):
    """Main trading dashboard screen."""
    
    def __init__(self, parent):
        super().__init__(parent, bg=config.COLORS['bg_primary'])
        self.pack(fill=tk.BOTH, expand=True)
        self.data_manager = DataManager()
        self.create_widgets()
        self.update_display()
    
    def create_widgets(self):
        """Create the main screen widgets."""
        # Title
        title_frame = tk.Frame(self, bg=config.COLORS['bg_primary'])
        title_frame.pack(fill=tk.X, pady=(10, 20))
        
        title_label = tk.Label(title_frame, text="SEN TRADING SYSTEM", 
                              font=('Arial', 24, 'bold'),
                              bg=config.COLORS['bg_primary'],
                              fg=config.COLORS['accent'])
        title_label.pack()
        
        # Main content area
        content_frame = tk.Frame(self, bg=config.COLORS['bg_primary'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Left panel - Stats and Chart
        left_panel = tk.Frame(content_frame, bg=config.COLORS['bg_primary'])
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        # Stats row
        self.create_stats_section(left_panel)
        
        # Chart section
        self.create_chart_section(left_panel)
        
        # Bottom section
        self.create_bottom_section(left_panel)
        
        # Right panel - Control and Strategies
        right_panel = tk.Frame(content_frame, bg=config.COLORS['bg_primary'])
        right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))
        
        # Control section
        self.create_control_section(right_panel)
        
        # Strategy section
        self.create_strategy_section(right_panel)
    
    def create_stats_section(self, parent):
        """Create the statistics section."""
        stats_frame = tk.Frame(parent, bg=config.COLORS['bg_primary'])
        stats_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Stats cards
        self.balance_card = StatCard(stats_frame, "Balance", "1215")
        self.balance_card.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.equity_card = StatCard(stats_frame, "Equity", "345") 
        self.equity_card.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.max_trade_card = StatCard(stats_frame, "Max_Trade", "5", "Set")
        self.max_trade_card.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        self.max_loss_card = StatCard(stats_frame, "Max_Loss", "3%", "Set")
        self.max_loss_card.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
    
    def create_chart_section(self, parent):
        """Create the chart section."""
        chart_frame = tk.Frame(parent, bg=config.COLORS['bg_secondary'], relief='raised', bd=1)
        chart_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Chart header
        header_frame = tk.Frame(chart_frame, bg=config.COLORS['bg_secondary'])
        header_frame.pack(fill=tk.X, padx=10, pady=5)
        
        tk.Label(header_frame, text="Open Position", font=('Arial', 12, 'bold'),
                bg=config.COLORS['bg_secondary']).pack(side=tk.LEFT)
        
        # Profit display
        profit_frame = tk.Frame(chart_frame, bg=config.COLORS['bg_secondary'])
        profit_frame.pack(fill=tk.X, padx=10)
        
        tk.Label(profit_frame, text="58%", font=('Arial', 24, 'bold'),
                bg=config.COLORS['bg_secondary'], 
                fg=config.COLORS['success']).pack(side=tk.LEFT)
        tk.Label(profit_frame, text="Total profit/loss", font=('Arial', 10),
                bg=config.COLORS['bg_secondary'],
                fg=config.COLORS['text_secondary']).pack(side=tk.LEFT, padx=(10, 0))
        
        # Today's profit
        tk.Label(profit_frame, text="6%", font=('Arial', 14, 'bold'),
                bg=config.COLORS['bg_secondary'],
                fg=config.COLORS['success']).pack(side=tk.LEFT, padx=(20, 0))
        tk.Label(profit_frame, text="Today profit/loss", font=('Arial', 8),
                bg=config.COLORS['bg_secondary'],
                fg=config.COLORS['text_secondary']).pack(side=tk.LEFT, padx=(5, 0))
        
        # Chart
        self.profit_chart = ProfitChart(chart_frame)
        self.profit_chart.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def create_bottom_section(self, parent):
        """Create the bottom section with connection and terminal."""
        bottom_frame = tk.Frame(parent, bg=config.COLORS['bg_primary'])
        bottom_frame.pack(fill=tk.X)
        
        # Connection config
        conn_frame = tk.Frame(bottom_frame, bg=config.COLORS['bg_secondary'], 
                             relief='raised', bd=1, height=100)
        conn_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        tk.Label(conn_frame, text="CONNECTION_CONFIG", font=('Arial', 10, 'bold'),
                bg=config.COLORS['bg_secondary']).pack(pady=10)
        
        # MT5 Terminal
        terminal_frame = tk.Frame(bottom_frame, bg=config.COLORS['bg_secondary'],
                                 relief='raised', bd=1, height=100)
        terminal_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        tk.Label(terminal_frame, text="MT5 TERMINAL", font=('Arial', 10, 'bold'),
                bg=config.COLORS['bg_secondary']).pack(pady=10)
    
    def create_control_section(self, parent):
        """Create the control section."""
        control_frame = tk.Frame(parent, bg=config.COLORS['bg_secondary'],
                                relief='raised', bd=1, width=250)
        control_frame.pack(fill=tk.X, pady=(0, 20))
        control_frame.pack_propagate(False)
        
        # Drawdown display
        tk.Label(control_frame, text="Drawdown: 0.00%", font=('Arial', 10),
                bg=config.COLORS['bg_secondary']).pack(pady=5)
        tk.Label(control_frame, text="Trades: 0", font=('Arial', 10),
                bg=config.COLORS['bg_secondary']).pack(pady=5)
        
        # Start/Stop button
        self.start_button = tk.Button(control_frame, text="START", 
                                     font=('Arial', 12, 'bold'),
                                     bg=config.COLORS['accent'],
                                     fg='white', width=15, height=2,
                                     command=self.toggle_trading)
        self.start_button.pack(pady=10)
        
        # Account info
        tk.Label(control_frame, text="OFC_ID", font=('Arial', 8),
                bg=config.COLORS['bg_secondary']).pack()
        tk.Label(control_frame, text="ABCDEFGHI", font=('Arial', 10, 'bold'),
                bg=config.COLORS['bg_secondary']).pack()
        
        tk.Label(control_frame, text="OFC RUNNING.../OFC STOPPING", font=('Arial', 8),
                bg=config.COLORS['bg_secondary']).pack(pady=(10, 5))
    
    def create_strategy_section(self, parent):
        """Create the strategy section."""
        self.strategy_list = StrategyList(parent, bg=config.COLORS['bg_secondary'],
                                         relief='raised', bd=1, width=250, height=300)
        self.strategy_list.pack(fill=tk.BOTH, expand=True)
        self.strategy_list.pack_propagate(False)
    
    def update_display(self):
        """Update the display with current data."""
        # Update stats
        account = self.data_manager.get_account_info()
        
        # Update chart
        profit_data = self.data_manager.get_profit_history()
        self.profit_chart.update_data(profit_data)
        
        # Update strategies
        strategies = self.data_manager.get_strategies()
        self.strategy_list.update_strategies(strategies)
        
        # Schedule next update
        self.after(config.CHART_UPDATE_INTERVAL, self.update_display)
    
    def toggle_trading(self):
        """Toggle trading start/stop."""
        current_text = self.start_button['text']
        if current_text == "START":
            self.start_button.configure(text="STOP", bg=config.COLORS['error'])
        else:
            self.start_button.configure(text="START", bg=config.COLORS['accent'])