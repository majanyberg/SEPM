import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

from PIL import Image, ImageTk
import os

# Attempt to import required modules
try:
    from game_logic_connector import GameLogicConnector
    from backend_connector import BackendConnector
    #from backend.user import get_user_profile, get_user_stats
    #from backend.words import get_words_from_category, get_times
    #from clock_logic.source.game.Game import Game
    #from clock_logic.source.state.State import State
    modules_loaded = True
except ImportError as e:
    print(f"Error: {e}")
    modules_loaded = False  # Prevent game from running if dependencies are missing

# Define the path to the custom Work Sans font
#font_path = "main/fonts/WorkSans.ttf"
font_path = "assets/Work_Sans/WorkSans-Italic-VariableFont_wght.ttf"

# Define paths dynamically
#ASSETS_PATH = os.path.join(os.getcwd(), "assets")
#FONT_PATH = os.path.join(ASSETS_PATH, "Work_Sans", "WorkSans-Italic-VariableFont_wght.ttf")
#IMAGE_PATH = os.path.join(ASSETS_PATH, "UU-logo")


class ClockGame:
    def __init__(self, root, return_to_main_menu_callback=None):
        """Initialize the Clock Game UI with an optional return-to-main callback."""
        self.root = root
        self.root.title("Clock Game")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)
        self.root.configure(bg='#FFFFFF')

        # Store the callback function to return to the Main Menu
        self.return_to_main_menu_callback = return_to_main_menu_callback

        # Register custom font if available
        try:
            self.custom_font = tkFont.Font(family="Work Sans", size=14, slant="italic")
        except Exception as e:
            print(f"Warning: Failed to load Work Sans font. Using default font. Error: {e}")
            self.custom_font = ("Arial", 14)  # Fallback to Arial

        if not modules_loaded:
            messagebox.showerror("Missing Dependencies", 
                "Required modules (game_logic_connector, backend_connector) are missing.")
            self.root.destroy()
            return

        # Connect to game logic and backend modules
        self.logic = GameLogicConnector()
        self.backend = BackendConnector()

        # Connect to game logic and backend modules once integration is correct
        #self.logic = Game()  # The actual game logic
        #self.backend = get_user_profile  # Fetch user profile
        #self.user_stats = get_user_stats()  # Fetch user statistics
        #self.words = get_words_from_category  # Fetch words/hints
        #self.times = get_times()  # Fetch time expressions

        # Flag to track UI initialization
        self.initialized = False  
        self.root.bind("<Configure>", self.resize_ui)

        # Load the game menu UI
        self.load_ui()

        # Delay marking as initialized to allow first UI setup
        self.root.after(100, self.mark_initialized)

    def mark_initialized(self):
        """Enable resizing after the first UI setup is done."""
        self.initialized = True  

    def load_ui(self):
        """Setup the UI components of the game."""
        self.menu_frame = tk.Frame(self.root, bg="#dbdbdb")
        self.menu_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Load background image (UU-logo)
        image_path = "assets/UU-logo"
        #image_path = "main/images/UU-logo" # Once integration is correct

        if os.path.exists(image_path):
            try:
                self.bg_image = Image.open(image_path).convert("RGBA")
                # Resize the image to 40% of its original size
                new_width = int(self.bg_image.width * 1)
                new_height = int(self.bg_image.height * 1)

                self.bg_image = self.bg_image.resize((new_width, new_height), Image.LANCZOS)
                self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)

                #self.bg_label = tk.Label(self.menu_frame, image=self.bg_image_tk)
                #self.bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
                self.bg_label = tk.Label(self.menu_frame, image=self.bg_image_tk, bg="#dbdbdb")

                # Center the smaller UU-logo at the top
                self.bg_label.place(relx=1.5, rely=1, anchor="center")
            except Exception as e:
                print(f"Error loading UU-logo: {e}")

        # Title Label
        self.title_label = tk.Label(self.menu_frame, text="CLOCK GAME", 
                                    font=(self.custom_font, 24, "italic"), fg="black", bg="#dbdbdb")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Level Buttons
        self.level_buttons = []
        for idx, level in enumerate(range(1, 4)):
            button = tk.Button(self.menu_frame, text=f"Level {level}", font=(self.custom_font, 14), 
                               bg="#8B0000", fg="white", relief="ridge", bd=3, 
                               command=lambda l=level: self.start_level(l))
            button.place(relx=0.5, rely=0.3 + (idx * 0.13), anchor="center")
            self.level_buttons.append(button)

        # Leaderboard Button
        self.leaderboard_button = tk.Button(self.menu_frame, text="Leaderboard", 
                                            font=(self.custom_font, 14), bg="#8B0000", fg="white", 
                                            relief="ridge", bd=3, command=self.show_leaderboard)
        self.leaderboard_button.place(relx=0.5, rely=0.7, anchor="center")

        # Reset Button
        self.reset_button = tk.Button(self.menu_frame, text="Reset Game", 
                                      font=(self.custom_font, 14), bg="gray", fg="white", 
                                      command=self.reset_game)
        self.reset_button.place(relx=0.5, rely=0.85, anchor="center")

        # Return to Main Menu Button
        self.return_button = tk.Button(self.menu_frame, text="Return to Main Menu",
                                       font=(self.custom_font, 14), bg="#8B0000", fg="white",
                                       relief="ridge", bd=3, command=self.return_to_main_menu)
        self.return_button.place(relx=0.5, rely=0.92, anchor="center")

        # Load saved progress from backend
        try:
            self.backend.load_progress()
        except FileNotFoundError:
            print("Warning: progress.json not found. Creating a new file.")
            #with open("main/images/progress.json", "w") as f:
            with open("assets/progress.json", "w") as f:
                f.write('{"scores": {}, "leaderboard": []}')

    def resize_ui(self, event):
        """Dynamically adjust UI elements when the window resizes, except on the first launch."""
        if not self.initialized:
            return  

        new_font_size = max(20, int(event.width / 40))
        self.title_label.config(font=(self.custom_font, new_font_size))

    def start_level(self, level):
        """Start a selected level, calling the logic module to manage game logic."""
        self.menu_frame.place_forget()
        self.logic.start_level(self.root, level, self.back_to_menu)

    def show_leaderboard(self):
        """Display leaderboard information."""
        scores = self.backend.get_leaderboard()
        messagebox.showinfo("Leaderboard", "\n".join(scores) if scores else "No scores yet!")

    def reset_game(self):
        """Reset game progress using backend module."""
        self.backend.reset_progress()
        messagebox.showinfo("Game Reset", "Game progress has been reset.")

    def back_to_menu(self):
        """Return to the game menu."""
        self.load_ui()

    def return_to_main_menu(self):
        """Handle returning to the main menu."""
        if self.return_to_main_menu_callback:
            self.return_to_main_menu_callback()
        else:
            self.root.destroy()  # Close Clock Game UI if no main menu is available
