import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
from source.fetchQA.FetchQA import load_image_from_url
from game_logic_connector import GameLogicConnector
import random

class Level1UI:
    def __init__(self, root, back_to_menu_callback, logic: GameLogicConnector):
        self.root = root
        self.back_to_menu_callback = back_to_menu_callback
        self.sizex = 800
        self.sizey = 600
        self.game_logic = logic
        self.score = self.game_logic.fetch_score()
        self.level = self.game_logic.game.game_state.level
        
        self.clock_image = None
        self.title_font = tkFont.Font(family="Arial", size=self.sizex//25, weight="bold")
        self.normal_font = tkFont.Font(family="Arial", size=20)
        
        self.top_bar_color = "#f5f5f5" 
        
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Clock Game - Level 1")
        self.root.geometry(f"{self.sizex}x{self.sizey}")

        self.create_top_bar()

        self.line_frame = tk.Frame(self.root, bg="black", height=2)
        self.line_frame.pack(fill="x")

        self.create_main_frame()

        self.create_bottom_bar()

        self.load_question()

    def create_top_bar(self):
        self.top_frame = tk.Frame(self.root, bg=self.top_bar_color, height=40)
        self.top_frame.pack(fill="x", side="top")
    
        self.top_content_frame = tk.Frame(self.top_frame, bg=self.top_bar_color)
        self.top_content_frame.pack(fill="x", expand=True)
    
        self.top_left_frame = tk.Frame(self.top_content_frame, bg=self.top_bar_color)
        self.top_left_frame.pack(side="left")
    
        self.uppsala_logo = tk.PhotoImage(file="assets/uu-logo.png")
        self.uppsala_label = tk.Label(self.top_left_frame,
                                      image=self.uppsala_logo,
                                      bg=self.top_bar_color)
        self.uppsala_label.pack(side="left", padx=20, pady=10)
    

        self.top_center_frame = tk.Frame(self.top_content_frame, bg=self.top_bar_color)
        self.top_center_frame.pack(side="left", expand=True)
    
        self.clock_game_label = tk.Label(self.top_center_frame,
                                         text="CLOCK GAME",
                                         bg=self.top_bar_color,
                                         fg="#C54549",
                                         font=self.title_font)
        self.clock_game_label.pack(anchor="center")
    

        self.top_right_frame = tk.Frame(self.top_content_frame, bg=self.top_bar_color)
        self.top_right_frame.pack(side="right")
    
        self.level_label = tk.Label(self.top_right_frame,
                                    text=f"Level {self.level}",
                                    bg=self.top_bar_color,
                                    fg="black",
                                    font=("Arial", 12))
        self.level_label.pack(side="right", padx=20, pady=10)

    def create_main_frame(self):
        # Main area (left answer buttons + right clock and Next button)
        self.main_frame = tk.Frame(self.root, bg="white")
        self.main_frame.pack(fill="both", expand=True)

        # Left: options and question, first create a main Frame
        self.left_frame = tk.Frame(self.main_frame, bg="white")
        self.left_frame.pack(side="left", fill="both", expand=True)

        # Create another Frame inside the left side for centering
        self.left_content_frame = tk.Frame(self.left_frame, bg="white")
        self.left_content_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Question label (placed in left_content_frame)
        self.question_label = tk.Label(self.left_content_frame, text="", font=("Arial", 26, "bold"), fg="#8B0000", bg="white")
        self.question_label.pack(pady=self.sizey//50)

        # Create option buttons
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.left_content_frame,
                            text=f"Option {i+1}",
                            font=self.normal_font,
                            bg="#cccccc",
                            fg="black",
                            width=self.sizex//50,
                            height=self.sizey//540,
                            command=lambda i=i: self.check_answer(i))
            btn.pack(pady=self.sizey//50)
            self.option_buttons.append(btn)

        # Right: clock icon + time label + Next button
        self.right_frame = tk.Frame(self.main_frame, bg="white")
        self.right_frame.pack(side="right", fill="both", expand=True)

        # Right internal Frame, center content
        self.right_content_frame = tk.Frame(self.right_frame, bg="white")
        self.right_content_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.clock_image = tk.PhotoImage(file="assets/Loading.png")
        self.clock_label = tk.Label(self.right_content_frame, image=self.clock_image, bg="white")
        # self.clock_label.pack(pady=self.sizey//144)

        # self.time_label = tk.Label(self.right_content_frame, text="8:00", font=("Arial", 16), bg="white", fg="black")
        # self.time_label.pack(pady=self.sizey//144)

        self.next_button = tk.Button(self.right_content_frame,
                                    text="Next",
                                    font=self.normal_font,
                                    bg="#cccccc",
                                    fg="black",
                                    width=self.sizex//50,
                                    height=self.sizey//540,
                                    command=self.load_question)
        self.next_button.pack(pady=self.sizey//72)

    def create_bottom_bar(self):
        # Bottom background: light gray
        self.bottom_frame = tk.Frame(self.root, bg=self.top_bar_color, height=400)
        self.bottom_frame.pack(fill="x", side="bottom")
    
        self.bottom_content_frame = tk.Frame(self.bottom_frame, bg=self.top_bar_color)
        self.bottom_content_frame.pack(fill="both", expand=True)
    
        # Left：Score
        self.bottom_left_frame = tk.Frame(self.bottom_content_frame, bg=self.top_bar_color)
        self.bottom_left_frame.pack(side="left")
    
        self.score_label = tk.Label(self.bottom_left_frame,
                                    text=f"Score: {self.score}",
                                    bg=self.top_bar_color,
                                    fg="black",
                                    font=("Arial", 12))
        self.score_label.pack(padx=20)
    
        # Center: Hint
        self.bottom_center_frame = tk.Frame(self.bottom_content_frame, bg=self.top_bar_color)
        self.bottom_center_frame.pack(side="left", expand=True)
    
        self.hint_button = tk.Button(self.bottom_center_frame,
                                     text="Hint",
                                     font=("Arial", 12),
                                     bg="#cccccc",
                                     fg="black",
                                     width=self.sizex//50,
                                     height=self.sizey//1080,
                                     command=self.game_logic.provide_hint())
        self.hint_button.pack(anchor="center")
    
        # Right: Home button
        self.bottom_right_frame = tk.Frame(self.bottom_content_frame, bg=self.top_bar_color)
        self.bottom_right_frame.pack(side="right")
    
        self.home_button = tk.Button(self.bottom_right_frame,
                                     text="🏠",
                                     font=("Arial", 12),
                                     bg="#cccccc",
                                     fg="black",
                                     width=self.sizex//50,
                                     height=self.sizey//1080,
                                     command=self.back_to_menu_callback)
        self.home_button.pack(padx=20)

    def load_question(self):
        question_data = self.game_logic.fetch_question(self.level)
        if question_data:
            if question_data == "No more question available.":
                messagebox.showinfo("Level Complete", "Congratulations! You've completed all questions.")
                self.back_to_menu_callback()
                return
            self.question_label.config(text=question_data["query"])
            
            self.clock_image = load_image_from_url(question_data["img_url"])
            if self.clock_image:
                self.clock_label = tk.Label(self.right_content_frame, image=self.clock_image, bg="white")
                self.clock_label.pack(pady=self.sizey//144)
            else:
                print("Error loading image from URL.")
            
            options = question_data.get("options", ["No options available"])
            self.game_logic.correct_answer = question_data["ans"]
            options.append(self.game_logic.correct_answer)
            random.shuffle(options)
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option, bg="#cccccc")
            
            # If you need to update the clock display, you can update self.time_label.config(text="...")

            # renew score
            self.score = self.game_logic.fetch_score()
        else:
            print("No question available.")

    def check_answer(self, index):
        selected_answer = self.option_buttons[index].cget("text")
        is_correct, self.score = self.game_logic.submit_answer(selected_answer)
        if is_correct:
            self.option_buttons[index].config(bg="green")
        else:
            self.option_buttons[index].config(bg="red")
            for button in self.option_buttons:
                if button.cget("text") == self.game_logic.correct_answer:
                    button.config(bg="green")

        
        self.score_label.config(text=f"Score: {self.score}")

        new_level = self.game_logic.update_level(self.score)
        if new_level == self.level:
            self.load_question()
        else:
            self.show_level_complete_message(new_level)
        
        return self.score

    def show_level_complete_message(self, new_level):
        messagebox.showinfo("Level Complete", f"Congratulations! You've completed Level {self.level}.\nYour score: {self.score}")
        self.level = new_level
        self.game_logic.end_game()
        # self.load_question()


# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry("1080x720")
#     app = Level1UI(root, lambda: print("Back to menu"))
#     root.mainloop()