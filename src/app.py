"""Main application class for the SEN Trading System."""

import tkinter as tk
from tkinter import ttk
import config
from src.screens.main_screen import MainScreen
from src.screens.settings_screen import SettingsScreen
from src.screens.strategy_screen import StrategyScreen

class TradingApp:
    """Main trading application controller."""
    
    def __init__(self, root):
        self.root = root
        self.current_screen = None
        self.setup_window()
        self.create_menu()
        self.show_main_screen()
    
    def setup_window(self):
        """Configure the main window."""
        self.root.title(config.APP_TITLE)
        self.root.geometry(config.WINDOW_SIZE)
        self.root.minsize(*config.MIN_WINDOW_SIZE)
        self.root.configure(bg=config.COLORS['bg_primary'])
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (1200 // 2)
        y = (self.root.winfo_screenheight() // 2) - (800 // 2)
        self.root.geometry(f"1200x800+{x}+{y}")
    
    def create_menu(self):
        """Create the application menu bar."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # View menu
        view_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="View", menu=view_menu)
        view_menu.add_command(label="Main Dashboard", command=self.show_main_screen)
        view_menu.add_command(label="Strategy Manager", command=self.show_strategy_screen)
        view_menu.add_command(label="Settings", command=self.show_settings_screen)
    
    def clear_screen(self):
        """Clear the current screen."""
        if self.current_screen:
            self.current_screen.destroy()
    
    def show_main_screen(self):
        """Display the main trading dashboard."""
        self.clear_screen()
        self.current_screen = MainScreen(self.root)
    
    def show_strategy_screen(self):
        """Display the strategy management screen."""
        self.clear_screen()
        self.current_screen = StrategyScreen(self.root)
    
    def show_settings_screen(self):
        """Display the settings screen."""
        self.clear_screen()
        self.current_screen = SettingsScreen(self.root)
    
    def run(self):
        """Start the application main loop."""
        self.root.mainloop()