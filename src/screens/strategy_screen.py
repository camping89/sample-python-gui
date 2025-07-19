"""Strategy management screen."""

import tkinter as tk
from tkinter import ttk, messagebox
import config
from src.utils.data_manager import DataManager

class StrategyScreen(tk.Frame):
    """Strategy management screen."""
    
    def __init__(self, parent):
        super().__init__(parent, bg=config.COLORS['bg_primary'])
        self.pack(fill=tk.BOTH, expand=True)
        self.data_manager = DataManager()
        self.create_widgets()
        self.load_strategies()
    
    def create_widgets(self):
        """Create the strategy screen widgets."""
        # Title
        title_frame = tk.Frame(self, bg=config.COLORS['bg_primary'])
        title_frame.pack(fill=tk.X, pady=(10, 20))
        
        tk.Label(title_frame, text="STRATEGY MANAGER", 
                font=('Arial', 20, 'bold'),
                bg=config.COLORS['bg_primary'],
                fg=config.COLORS['accent']).pack()
        
        # Main content
        content_frame = tk.Frame(self, bg=config.COLORS['bg_primary'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Strategy list
        self.create_strategy_list(content_frame)
        
        # Control buttons
        self.create_control_buttons(content_frame)
    
    def create_strategy_list(self, parent):
        """Create the strategy list table."""
        list_frame = tk.Frame(parent, bg=config.COLORS['bg_secondary'], relief='raised', bd=1)
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Headers
        headers = ['ID', 'Name', 'Symbol', 'Timeframe', 'Status', 'Profit', 'Trades']
        header_frame = tk.Frame(list_frame, bg=config.COLORS['bg_secondary'])
        header_frame.pack(fill=tk.X, padx=10, pady=5)
        
        for header in headers:
            tk.Label(header_frame, text=header, font=('Arial', 10, 'bold'),
                    bg=config.COLORS['bg_secondary'], width=12).pack(side=tk.LEFT, padx=5)
        
        # Strategy list
        self.strategy_frame = tk.Frame(list_frame, bg=config.COLORS['bg_primary'])
        self.strategy_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    
    def create_control_buttons(self, parent):
        """Create control buttons."""
        button_frame = tk.Frame(parent, bg=config.COLORS['bg_primary'])
        button_frame.pack(fill=tk.X)
        
        tk.Button(button_frame, text="Add Strategy", 
                 bg=config.COLORS['success'], fg='white',
                 command=self.add_strategy).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Remove Strategy",
                 bg=config.COLORS['error'], fg='white',
                 command=self.remove_strategy).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Start All",
                 bg=config.COLORS['accent'], fg='white',
                 command=self.start_all).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Stop All",
                 bg=config.COLORS['warning'], fg='white',
                 command=self.stop_all).pack(side=tk.LEFT, padx=5)
    
    def load_strategies(self):
        """Load and display strategies."""
        # Clear existing
        for widget in self.strategy_frame.winfo_children():
            widget.destroy()
        
        strategies = self.data_manager.get_strategies()
        for strategy in strategies:
            self.add_strategy_row(strategy)
    
    def add_strategy_row(self, strategy):
        """Add a strategy row to the list."""
        row_frame = tk.Frame(self.strategy_frame, bg=config.COLORS['bg_secondary'])
        row_frame.pack(fill=tk.X, pady=2)
        
        # Strategy data
        data = [strategy.id, strategy.name, strategy.symbol, 
                strategy.timeframe, strategy.status, 
                f"{strategy.profit:.1f}", str(strategy.trades_count)]
        
        for i, value in enumerate(data):
            if i == 4:  # Status column
                color = config.COLORS['success'] if value == 'ACTIVE' else config.COLORS['warning']
                label = tk.Label(row_frame, text=value, width=12, fg=color,
                               bg=config.COLORS['bg_secondary'])
            elif i == 5:  # Profit column
                color = config.COLORS['success'] if float(value) >= 0 else config.COLORS['error']
                label = tk.Label(row_frame, text=value, width=12, fg=color,
                               bg=config.COLORS['bg_secondary'])
            else:
                label = tk.Label(row_frame, text=value, width=12,
                               bg=config.COLORS['bg_secondary'])
            label.pack(side=tk.LEFT, padx=5)
    
    def add_strategy(self):
        """Add new strategy dialog."""
        messagebox.showinfo("Add Strategy", "Add strategy functionality would be implemented here")
    
    def remove_strategy(self):
        """Remove selected strategy."""
        messagebox.showinfo("Remove Strategy", "Remove strategy functionality would be implemented here")
    
    def start_all(self):
        """Start all strategies."""
        for strategy in self.data_manager.get_strategies():
            self.data_manager.update_strategy_status(strategy.id, "ACTIVE")
        self.load_strategies()
        messagebox.showinfo("Success", "All strategies started")
    
    def stop_all(self):
        """Stop all strategies."""
        for strategy in self.data_manager.get_strategies():
            self.data_manager.update_strategy_status(strategy.id, "INACTIVE")
        self.load_strategies()
        messagebox.showinfo("Success", "All strategies stopped")