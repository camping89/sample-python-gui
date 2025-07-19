"""Custom widgets for the trading application."""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import config

class StatCard(tk.Frame):
    """A card widget for displaying statistics."""
    
    def __init__(self, parent, title, value, subtitle="", **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(bg=config.COLORS['bg_secondary'], relief='raised', bd=1)
        
        # Title
        title_label = tk.Label(self, text=title, font=('Arial', 10), 
                              bg=config.COLORS['bg_secondary'], 
                              fg=config.COLORS['text_secondary'])
        title_label.pack(pady=(10, 0))
        
        # Value
        value_label = tk.Label(self, text=str(value), font=('Arial', 16, 'bold'),
                              bg=config.COLORS['bg_secondary'],
                              fg=config.COLORS['text_primary'])
        value_label.pack(pady=(5, 0))
        
        # Subtitle
        if subtitle:
            subtitle_label = tk.Label(self, text=subtitle, font=('Arial', 8),
                                    bg=config.COLORS['bg_secondary'],
                                    fg=config.COLORS['text_secondary'])
            subtitle_label.pack(pady=(0, 10))

class ProfitChart(tk.Frame):
    """Chart widget for displaying profit data."""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.figure, self.ax = plt.subplots(figsize=(6, 3))
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Style the chart
        self.figure.patch.set_facecolor(config.COLORS['bg_secondary'])
        self.ax.set_facecolor(config.COLORS['bg_secondary'])
    
    def update_data(self, data):
        """Update chart with new data."""
        self.ax.clear()
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        profits = [d.profit for d in data]
        
        bars = self.ax.bar(days, profits, color=config.COLORS['accent'])
        self.ax.set_ylabel('Profit')
        self.ax.set_title('Daily Profit/Loss')
        
        # Color bars based on profit/loss
        for i, bar in enumerate(bars):
            if profits[i] < 0:
                bar.set_color(config.COLORS['error'])
            else:
                bar.set_color(config.COLORS['success'])
        
        self.canvas.draw()

class StrategyList(tk.Frame):
    """Widget for displaying strategy list."""
    
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.create_widgets()
    
    def create_widgets(self):
        """Create the strategy list widgets."""
        # Header
        header_frame = tk.Frame(self, bg=config.COLORS['bg_secondary'])
        header_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(header_frame, text="STRATEGIES", font=('Arial', 12, 'bold'),
                bg=config.COLORS['bg_secondary'], 
                fg=config.COLORS['text_primary']).pack(side=tk.LEFT)
        
        # Strategy list frame
        self.list_frame = tk.Frame(self, bg=config.COLORS['bg_primary'])
        self.list_frame.pack(fill=tk.BOTH, expand=True)
    
    def update_strategies(self, strategies):
        """Update the strategy list."""
        # Clear existing items
        for widget in self.list_frame.winfo_children():
            widget.destroy()
        
        # Add strategies
        for i, strategy in enumerate(strategies):
            self.add_strategy_item(strategy, i)
    
    def add_strategy_item(self, strategy, index):
        """Add a single strategy item."""
        item_frame = tk.Frame(self.list_frame, bg=config.COLORS['bg_secondary'], 
                             relief='raised', bd=1)
        item_frame.pack(fill=tk.X, padx=5, pady=2)
        
        # Strategy number
        tk.Label(item_frame, text=str(index + 1), width=3,
                bg=config.COLORS['bg_secondary']).pack(side=tk.LEFT, padx=5)
        
        # Strategy name
        tk.Label(item_frame, text=strategy.name, width=25, anchor='w',
                bg=config.COLORS['bg_secondary']).pack(side=tk.LEFT, padx=5)
        
        # Status
        status_color = config.COLORS['success'] if strategy.status == 'ACTIVE' else config.COLORS['warning']
        tk.Label(item_frame, text=strategy.status, width=10,
                bg=config.COLORS['bg_secondary'], 
                fg=status_color).pack(side=tk.RIGHT, padx=5)