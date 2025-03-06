# Attempt to import required modules
try:
    from game_logic_connector import GameLogicConnector
    from backend_connector import BackendConnector
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import font as tkFont
    from PIL import ImageFont, Image, ImageTk
    import os
    from levels.level1_ui import Level1UI
    from levels.level2_ui import Level2UI
    from levels.level3_ui import Level3UI
    modules_loaded = True
except ImportError as e:
    print(f"Error: {e}")
    modules_loaded = False  # Prevent game from running if dependencies are missing

# Define paths dynamically
ASSETS_PATH = os.path.join(os.getcwd(), "assets")
FONT_PATH = os.path.join(ASSETS_PATH, "WorkSans-Italic-VariableFont_wght.ttf")
IMAGE_PATH = os.path.join(ASSETS_PATH, "UU-logo")


class ClockGame:
    def __init__(self, root, return_to_main_menu_callback=None):
        """Initialize the Clock Game UI with an optional return-to-main callback."""
        self.root = root
        self.root.title("Clock Game")
        self.root.geometry("800x600") # Width & height
        self.root.minsize(600, 400) # Minimum width & height
        self.root.configure(bg='#FFFFFF')

        if not modules_loaded:
            messagebox.showerror("Missing Dependencies", 
                "Required modules are missing.")
            self.root.destroy()
            return
        
        # Initialize attributes
        self.bg_image = None
        self.bg_image_tk = None
        self.last_width = 800  # Store last width to avoid redundant resizing
        self.last_height = 600  # Store last height to avoid redundant resizing

        # Store the callback function to return to the Main Menu
        self.return_to_main_menu_callback = return_to_main_menu_callback

        # Attempt to load and register the custom font
        self.custom_font_family = self.load_custom_font(FONT_PATH, 14)

        # Load the game menu UI
        self.load_ui()

        # Connect to module
        self.backend = BackendConnector()
        self.logic = GameLogicConnector()

        # Flag to track UI initialization
        self.initialized = False  
        self.root.bind("<Configure>", self.resize_ui)

        # Delay marking as initialized to allow first UI setup
        self.root.after(100, self.mark_initialized)
        
    def load_custom_font(self, FONT_PATH, size):
        """Loads a TTF font from a file and registers it in Tkinter."""
        if os.path.exists(FONT_PATH):
            try:
                # Load the font using PIL to verify it's valid
                _ = ImageFont.truetype(FONT_PATH, size)

                # Register the font in Tkinter
                font_name = "CustomWorkSans"
                tkFont.Font(family=font_name, size=size)  # Register custom font

                return font_name  # Use the registered font name in Tkinter
            except Exception as e:
                print(f"Warning: Failed to load custom font. Error: {e}")

        print(f"Warning: Font file not found at {FONT_PATH}. Using default font.")
        return "Arial"  # Fallback to a default font

    def load_image(self, image_path, parent, relx=0.5, rely=0.1):
        """
        Loads an image, resizes it dynamically, and returns a Tkinter Label widget.
        :param image_path: Path to the image file.
        :param parent: Parent widget where the image will be placed.
        :param relx: Relative x-position of the image.
        :param rely: Relative y-position of the image.
        :return: Tkinter Label widget containing the image.
        """
        if os.path.exists(image_path):
            try:
                # Load and convert the image
                self.bg_image = Image.open(image_path).convert("RGBA")

                # Convert to Tkinter image format
                self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)  # Assign the image to self.bg_image_tk

                # Create and place the label
                label = tk.Label(parent, image=self.bg_image_tk, bg="#dbdbdb")
                label.image = self.bg_image_tk  # Prevent garbage collection
                label.place(relx=relx, rely=rely, anchor="center")

                return label  # Return the label for further manipulation if needed

            except Exception as e:
                print(f"Error loading image '{image_path}': {e}")

        else:
            print(f"Warning: Image file not found at {image_path}.")
            return None
        
        
    def mark_initialized(self):
        """Enable resizing after the first UI setup is done."""
        self.initialized = True  

    def load_ui(self):
        """Setup the UI components of the game."""
        self.menu_frame = tk.Frame(self.root, bg="#dbdbdb")
        self.menu_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Load the background image AFTER creating the menu frame
        self.bg_label = self.load_image(IMAGE_PATH, self.menu_frame, relx=1, rely=1)
        
        # Title Label
        self.title_label = tk.Label(self.menu_frame, text="CLOCK GAME", 
                                    font=(self.custom_font_family, 24, "italic"), fg="black", bg="#dbdbdb")
        self.title_label.place(relx=0.5, rely=0.1, anchor="center")

        # Level Buttons
        self.level_buttons = []
        for idx, level in enumerate(range(1, 4)):
            button = tk.Button(self.menu_frame, text=f"Level {level}", font=(self.custom_font_family, 14), 
                               bg="#8B0000", fg="white", relief="ridge", bd=3, 
                               command=lambda l=level: self.start_level(l))
            button.place(relx=0.5, rely=0.3 + (idx * 0.13), anchor="center")
            self.level_buttons.append(button)

        # Leaderboard Button
        self.leaderboard_button = tk.Button(self.menu_frame, text="Leaderboard", 
                                            font=(self.custom_font_family, 14), bg="#8B0000", fg="white", 
                                            relief="ridge", bd=3, command=self.show_leaderboard)
        self.leaderboard_button.place(relx=0.5, rely=0.7, anchor="center")

        # Reset Button
        self.reset_button = tk.Button(self.menu_frame, text="Reset Game", 
                                      font=(self.custom_font_family, 14), bg="gray", fg="white", 
                                      command=self.reset_game)
        self.reset_button.place(relx=0.5, rely=0.85, anchor="center")

        # Return to Main Menu Button
        self.return_button = tk.Button(self.menu_frame, text="Return to Main Menu",
                                       font=(self.custom_font_family, 14), bg="#8B0000", fg="white",
                                       relief="ridge", bd=3, command=self.return_to_main_menu)
        self.return_button.place(relx=0.5, rely=0.92, anchor="center")

        # Load saved progress from backend
        # try:
        #     self.backend.load_progress()
        # except FileNotFoundError:
        #     print("Warning: progress.json not found. Creating a new file.")
        #     #with open("main/images/progress.json", "w") as f:
        #     with open("assets/progress.json", "w") as f:
        #         f.write('{"scores": {}, "leaderboard": []}')

    def resize_ui(self, event):
        """Dynamically adjust UI elements when the window resizes, except on the first launch."""
        if not self.initialized:
            return  
        
        # Get current window size
        new_width, new_height = self.root.winfo_width(), self.root.winfo_height()

        # Only resize if dimensions have changed
        if (new_width, new_height) == (self.last_width, self.last_height):
            return  # Exit if the size hasn't changed

        # Update stored dimensions
        self.last_width, self.last_height = new_width, new_height

        print(f"Resizing: {new_width}x{new_height}")  # Debugging print statement

        # Resize Title Label Font
        new_font_size = max(24, min(48, int(new_width / 25)))  # Between 24 and 48px
        self.title_label.config(font=(self.custom_font_family, new_font_size))

        # Dynamically adjust button font size
        button_font_size = max(12, min(20, int(new_width / 55)))  # Keep font size between 12-20px
        new_button_font = (self.custom_font_family, button_font_size)

        print(f"New Button Font Size: {button_font_size}")  # Debugging print statement
    
        for button in self.level_buttons:
            button.config(font=new_button_font)

        self.leaderboard_button.config(font=new_button_font)
        self.reset_button.config(font=new_button_font)
        self.return_button.config(font=new_button_font)

        # Resize Home Button
        new_button_size = max(12, int(event.width / 80))  # Scale home button icon
        if hasattr(self, "level_frame"):  # Check if level_frame exists
            for widget in self.level_frame.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget("text") == "🏠":
                    widget.config(font=("Work Sans", new_button_size))


    def start_level(self, level):
        """Start a selected level, calling the logic module to manage game logic."""
        self.menu_frame.place_forget()

        # Clear previous level UI if it exists
        if hasattr(self, "current_level_ui") and self.current_level_ui:
            for widget in self.root.winfo_children():
                widget.destroy()  # Remove existing widgets
        level_ui_classes = {1: Level1UI, 2: Level2UI, 3: Level3UI}
        level_ui_class = level_ui_classes.get(level)

        if level_ui_class:
            self.current_level_ui = level_ui_class(self.root, self.back_to_menu, self.logic)
        else:
            messagebox.showinfo("Info", f"Level {level} is not yet implemented.")

    def show_leaderboard(self):
        """Display leaderboard information."""
        scores = self.backend.get_leaderboard()
        messagebox.showinfo("Leaderboard", "\n".join(scores) if scores else "No scores yet!")

    def reset_game(self):
        """Reset game progress using backend module."""
        self.backend.reset_progress()
        messagebox.showinfo("Game Reset", "Game progress has been reset.")

    def back_to_menu(self):
        """Return to the main menu by clearing level UI and reloading the menu."""
        # Clear Level UI
        if hasattr(self, "current_level_ui") and self.current_level_ui:
            for widget in self.root.winfo_children():
                widget.destroy()  # Destroy all widgets in the root window
        self.load_ui()

    def return_to_main_menu(self):
        """Handle returning to the main menu."""
        if self.return_to_main_menu_callback:
            self.return_to_main_menu_callback()
        else:
            self.root.destroy()  # Close Clock Game UI if no main menu is available
