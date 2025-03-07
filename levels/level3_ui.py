import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
from game_logic_connector import GameLogicConnector
import os


class Level3UI:
    def __init__(self, root, back_to_menu_callback):
        self.root = root
        self.back_to_menu_callback = back_to_menu_callback
        self.game_logic = GameLogicConnector()
        self.score = self.game_logic.fetch_score()
        self.level = 3
        self.font = tkFont.Font(family="Arial", size=20)
        self.keyboard_visible = False  # Track keyboard state
        self.setup_ui()

    def setup_ui(self):
        self.create_level_frame()
        self.create_home_button()
        self.create_score_label()
        self.create_question_label()
        self.create_input_field()
        self.create_submit_button()
        self.create_keyboard_toggle_button()
        self.create_virtual_keyboard()
        self.load_question()

    def create_level_frame(self):
        self.level_frame = tk.Frame(self.root, bg="white")
        self.level_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def create_home_button(self):
        home_button = tk.Button(self.level_frame, text="🏠", font=self.font, bg="#8B0000", fg="white", 
                                relief="ridge", bd=3, command=self.back_to_menu_callback)
        home_button.place(relx=0.95, rely=0.05, anchor="center")

    def create_score_label(self):
        self.score_label = tk.Label(self.level_frame, text=f"Score: {self.score}", font=self.font, fg="#8B0000", bg="white")
        self.score_label.place(relx=0.1, rely=0.05, anchor="w")

    def create_question_label(self):
        self.question_label = tk.Label(self.level_frame, text="", font=("Arial", 28), fg="#8B0000", bg="white")
        self.question_label.place(relx=0.5, rely=0.4, anchor="center")

    def create_input_field(self):
        self.answer_entry = tk.Entry(self.level_frame, font=self.font, justify="center", bg="lightgray", width=15)
        self.answer_entry.place(relx=0.5, rely=0.5, anchor="center")

    def create_submit_button(self):
        submit_button = tk.Button(self.level_frame, text="Submit", font=self.font, bg="gray", fg="white", 
                                  relief="ridge", bd=3, command=self.check_answer)
        submit_button.place(relx=0.5, rely=0.6, anchor="center", width=150, height=50)

    def create_keyboard_toggle_button(self):
        self.keyboard_button = tk.Button(self.level_frame, text="⌨️", font=self.font, bg="gray", fg="white", 
                                         relief="ridge", bd=3, command=self.toggle_keyboard)
        self.keyboard_button.place(relx=0.05, rely=0.05, anchor="center")

    def create_virtual_keyboard(self):
        self.keyboard_frame = tk.Frame(self.level_frame, bg="lightgray")
        swedish_keys = ['å', 'ä', 'ö', 'Å', 'Ä', 'Ö']

        for i, key in enumerate(swedish_keys):
            button = tk.Button(self.keyboard_frame, text=key, font=self.font, bg="white", fg="black", 
                               width=5, height=2, command=lambda k=key: self.insert_character(k))
            button.grid(row=0, column=i, padx=5, pady=5)

    def toggle_keyboard(self):
        if self.keyboard_visible:
            self.keyboard_frame.place_forget()
        else:
            self.keyboard_frame.place(relx=0.05, rely=0.15)
        self.keyboard_visible = not self.keyboard_visible

    def insert_character(self, char):
        self.answer_entry.insert(tk.END, char)

    def load_question(self):
        self.question_label.config(text=self.game_logic.fetch_question(self.level))

    def check_answer(self):
        selected_answer = self.answer_entry.get()
        is_correct, self.score = self.game_logic.submit_answer(selected_answer)

        if is_correct:
            self.answer_entry.config(bg="green")
        else:
            self.answer_entry.config(bg="red")

        self.score_label.config(text=f"Score: {self.score}")

        new_level = self.game_logic.update_level(self.score)
        if new_level == self.level:
            self.load_question()
        else:
            self.show_level_complete_message(new_level)

    def show_level_complete_message(self, new_level):
        messagebox.showinfo("Level Complete", f"Congratulations! You've completed Level {self.level}.\nYour score: {self.score}")
        self.level = new_level
        self.load_question()

# 🔹 Run the application
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1080x720")
    app = Level3UI(root, lambda: print("Back to menu"))
    root.mainloop()