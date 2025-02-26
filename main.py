""" Required Function from Main Menu
Function	        Purpose
start_clock_game()	Initializes the Clock Game from the main menu."""

import tkinter as tk
from ui import ClockGame

def open_main_menu():
    """Reopen the Main Menu when returning from Clock Game."""
    print("Returning to Main Menu...")  # Replace with actual main menu function

def start_clock_game():
    """Start the Clock Game UI from the Main Menu."""
    root = tk.Tk()
    game = ClockGame(root, return_to_main_menu_callback=open_main_menu)
    root.mainloop()

#def start_clock_game():
#    """This function will be called from the Main Menu to start the Clock Game."""
#    root = tk.Tk()
#    game = ClockGame(root)
#    root.mainloop()

if __name__ == "__main__":
    start_clock_game()
    #print("Clock Game UI module loaded. Call start_clock_game() to start.")

