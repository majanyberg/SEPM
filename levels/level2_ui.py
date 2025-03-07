import tkinter as tk
from tkinter import font as tkFont, messagebox
from game_logic_connector import GameLogicConnector
from source.fetchQA.FetchQA import load_image_from_url
import random
import os

class Level2UI:
    def __init__(self, root, back_to_menu_callback, logic: GameLogicConnector):
        self.root = root
        self.back_to_menu_callback = back_to_menu_callback
        self.game_logic = logic
        self.score = self.game_logic.fetch_score()
        self.level = self.game_logic.game.game_state.level
        self.clock_image_path = "assets/Loading.png"
        self.font = tkFont.Font(family="Arial", size=20)
        self.setup_ui()

    def setup_ui(self):
        self.create_level_frame()
        self.create_home_button()
        self.create_score_label()
        self.create_clock_label()
        self.create_question_label()
        self.create_input_field()
        self.create_action_buttons()
        self.create_virtual_keyboard()
        self.load_question()

    def create_level_frame(self):
        self.level_frame = tk.Frame(self.root, bg="white")
        self.level_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def create_home_button(self):
        home_button = tk.Button(self.level_frame, text="🏠", font=self.font, bg="#8B0000", fg="white", relief="ridge", bd=3, command=self.back_to_menu_callback)
        home_button.place(relx=0.95, rely=0.05, anchor="center")

    def create_score_label(self):
        self.score_label = tk.Label(self.level_frame, text=f"Score: {self.score}", font=self.font, fg="#8B0000", bg="white")
        self.score_label.place(relx=0.1, rely=0.05, anchor="w")

    def create_clock_label(self):
        if os.path.isfile(self.clock_image_path):
            self.clock_image = tk.PhotoImage(file=self.clock_image_path)
            self.clock_label = tk.Label(self.level_frame, image=self.clock_image, bg="white")
        else:
            self.clock_label = tk.Label(self.level_frame, text="(No Clock Image Found)", font=("Arial", 14), fg="red", bg="white")
        self.clock_label.place(relx=0.75, rely=0.3, anchor="center")

    def create_question_label(self):
        self.question_label = tk.Label(self.level_frame, text="", font=("Arial", 28), fg="#8B0000", bg="white")
        self.question_label.place(relx=0.5, rely=0.1, anchor="center")

    def create_input_field(self):
        self.user_input = tk.Entry(self.level_frame, font=self.font, width=20)
        self.user_input.place(relx=0.5, rely=0.5, anchor="center")
    
    def create_action_buttons(self):
        submit_btn = tk.Button(self.level_frame, text="Submit", font=self.font, bg="#90EE90", command=self.submit_answer)
        submit_btn.place(relx=0.35, rely=0.6, anchor="center", width=120, height=40)
        
        clear_btn = tk.Button(self.level_frame, text="Clear", font=self.font, bg="#FFB6C1", command=lambda: self.user_input.delete(0, tk.END))
        clear_btn.place(relx=0.65, rely=0.6, anchor="center", width=120, height=40)
    
    def create_virtual_keyboard(self):
        words = ["en/ett", "två", "...", "över", "halv", "i"]
        keyboard_frame = tk.Frame(self.level_frame, bg="#F0F0F0")
        keyboard_frame.place(relx=0.5, rely=0.75, anchor="center")
        for i, word in enumerate(words):
            btn = tk.Button(keyboard_frame, text=word, font=("Arial", 14), bg="lightgray", command=lambda w=word: self.insert_text(w))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)

    def insert_text(self, text):
        self.user_input.insert(tk.END, text + " ")
    
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
                self.clock_label.config(image=self.clock_image)
                self.clock_label.image = self.clock_image
            else:
                print("Error loading image from URL.")
        else:
            print("No question available.")
    
    def submit_answer(self):
        answer = self.user_input.get().strip()
        is_correct, self.score = self.game_logic.submit_answer(answer)
        self.score_label.config(text=f"Score: {self.score}")
        if is_correct:
            messagebox.showinfo("Correct!", "Well done!")
        else:
            messagebox.showinfo("Wrong!", "Try again.")
        self.user_input.delete(0, tk.END)
        new_level = self.game_logic.update_level(self.score)
        if new_level <= self.level:
            self.load_question()
        else:
            self.show_level_complete_message(new_level)
    
    def show_level_complete_message(self, new_level):
        messagebox.showinfo("Level Complete", f"Congratulations! You've completed Level {self.level}.\nYour score: {self.score}")
        self.level = new_level
        self.game_logic.end_game()
