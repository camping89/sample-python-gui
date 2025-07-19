"""Settings and configuration screen."""

import tkinter as tk
from tkinter import ttk, messagebox
import config

class SettingsScreen(tk.Frame):
    """Settings and configuration screen."""
    
    def __init__(self, parent):
        super().__init__(parent, bg=config.COLORS['bg_primary'])
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()
    
    def create_widgets(self):
        """Create the settings screen widgets."""
        # Title
        title_frame = tk.Frame(self, bg=config.COLORS['bg_primary'])
        title_frame.pack(fill=tk.X, pady=(10, 20))
        
        tk.Label(title_frame, text="SETTINGS", 
                font=('Arial', 20, 'bold'),
                bg=config.COLORS['bg_primary'],
                fg=config.COLORS['accent']).pack()
        
        # Main content
        content_frame = tk.Frame(self, bg=config.COLORS['bg_primary'])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=20)
        
        # Create sections
        self.create_trading_settings(content_frame)
        self.create_connection_settings(content_frame)
        self.create_display_settings(content_frame)
    
    def create_trading_settings(self, parent):
        """Create trading settings section."""
        section_frame = tk.LabelFrame(parent, text="Trading Settings", 
                                     bg=config.COLORS['bg_secondary'],
                                     font=('Arial', 12, 'bold'))
        section_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Max trades
        tk.Label(section_frame, text="Max Trades:", 
                bg=config.COLORS['bg_secondary']).grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.max_trades_var = tk.StringVar(value=str(config.MAX_TRADES))
        tk.Entry(section_frame, textvariable=self.max_trades_var, width=10).grid(row=0, column=1, padx=10, pady=5)
        
        # Max loss
        tk.Label(section_frame, text="Max Loss %:", 
                bg=config.COLORS['bg_secondary']).grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.max_loss_var = tk.StringVar(value=str(config.MAX_LOSS_PERCENT))
        tk.Entry(section_frame, textvariable=self.max_loss_var, width=10).grid(row=1, column=1, padx=10, pady=5)
        
        # Default balance
        tk.Label(section_frame, text="Default Balance:", 
                bg=config.COLORS['bg_secondary']).grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.balance_var = tk.StringVar(value=str(config.DEFAULT_BALANCE))
        tk.Entry(section_frame, textvariable=self.balance_var, width=10).grid(row=2, column=1, padx=10, pady=5)
    
    def create_connection_settings(self, parent):
        """Create connection settings section."""
        section_frame = tk.LabelFrame(parent, text="Connection Settings", 
                                     bg=config.COLORS['bg_secondary'],
                                     font=('Arial', 12, 'bold'))
        section_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Server
        tk.Label(section_frame, text="MT5 Server:", 
                bg=config.COLORS['bg_secondary']).grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.server_var = tk.StringVar(value="MetaQuotes-Demo")
        tk.Entry(section_frame, textvariable=self.server_var, width=20).grid(row=0, column=1, padx=10, pady=5)
        
        # Login
        tk.Label(section_frame, text="Login:", 
                bg=config.COLORS['bg_secondary']).grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.login_var = tk.StringVar()
        tk.Entry(section_frame, textvariable=self.login_var, width=20).grid(row=1, column=1, padx=10, pady=5)
        
        # Password
        tk.Label(section_frame, text="Password:", 
                bg=config.COLORS['bg_secondary']).grid(row=2, column=0, sticky='w', padx=10, pady=5)
        self.password_var = tk.StringVar()
        tk.Entry(section_frame, textvariable=self.password_var, width=20, show='*').grid(row=2, column=1, padx=10, pady=5)
    
    def create_display_settings(self, parent):
        """Create display settings section."""
        section_frame = tk.LabelFrame(parent, text="Display Settings", 
                                     bg=config.COLORS['bg_secondary'],
                                     font=('Arial', 12, 'bold'))
        section_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Chart update interval
        tk.Label(section_frame, text="Chart Update (ms):", 
                bg=config.COLORS['bg_secondary']).grid(row=0, column=0, sticky='w', padx=10, pady=5)
        self.update_interval_var = tk.StringVar(value=str(config.CHART_UPDATE_INTERVAL))
        tk.Entry(section_frame, textvariable=self.update_interval_var, width=10).grid(row=0, column=1, padx=10, pady=5)
        
        # Default timeframe
        tk.Label(section_frame, text="Default Timeframe:", 
                bg=config.COLORS['bg_secondary']).grid(row=1, column=0, sticky='w', padx=10, pady=5)
        self.timeframe_var = tk.StringVar(value=config.DEFAULT_TIMEFRAME)
        timeframe_combo = ttk.Combobox(section_frame, textvariable=self.timeframe_var, 
                                      values=['M1', 'M5', 'M15', 'M30', 'H1', 'H4', 'D1'], width=8)
        timeframe_combo.grid(row=1, column=1, padx=10, pady=5)
        
        # Save and Reset buttons
        button_frame = tk.Frame(section_frame, bg=config.COLORS['bg_secondary'])
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        tk.Button(button_frame, text="Save Settings", 
                 bg=config.COLORS['success'], fg='white',
                 command=self.save_settings).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Reset to Defaults",
                 bg=config.COLORS['warning'], fg='white',
                 command=self.reset_settings).pack(side=tk.LEFT, padx=5)
    
    def save_settings(self):
        """Save current settings."""
        try:
            # Validate inputs
            max_trades = int(self.max_trades_var.get())
            max_loss = float(self.max_loss_var.get())
            balance = float(self.balance_var.get())
            update_interval = int(self.update_interval_var.get())
            
            # Save settings (in a real app, this would persist to file)
            messagebox.showinfo("Success", "Settings saved successfully!")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values")
    
    def reset_settings(self):
        """Reset settings to defaults."""
        self.max_trades_var.set(str(config.MAX_TRADES))
        self.max_loss_var.set(str(config.MAX_LOSS_PERCENT))
        self.balance_var.set(str(config.DEFAULT_BALANCE))
        self.update_interval_var.set(str(config.CHART_UPDATE_INTERVAL))
        self.timeframe_var.set(config.DEFAULT_TIMEFRAME)
        self.server_var.set("MetaQuotes-Demo")
        self.login_var.set("")
        self.password_var.set("")
        
        messagebox.showinfo("Success", "Settings reset to defaults")