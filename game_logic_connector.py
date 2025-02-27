""" Required Functions from Clock Logic Module
Function	                                    Purpose
fetch_question(level: int) -> str	            Retrieves a time-related question based on difficulty level.
validate_answer(user_answer: str) -> bool	    Checks if the user's answer is correct.
provide_hint() -> str	                        Returns a hint for the current question.
start_level(root, level, back_to_menu_callback)	Manages the UI and logic for each level."""

import random
import tkinter as tk


class GameLogicConnector:
    def start_level(self, root, level, back_to_menu_callback):
        """Initialize a game level."""
        self.level_frame = tk.Frame(root, bg="white")
        self.level_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        home_button = tk.Button(self.level_frame, text="🏠", font=("Work Sans", 14), bg="#8B0000", fg="white", 
                                relief="ridge", bd=3, command=back_to_menu_callback)
        home_button.place(relx=0.95, rely=0.05, anchor="center")

        self.correct_answer = self.fetch_question(level)
        
        self.level_label = tk.Label(self.level_frame, text=f"Level {level}", font=("Work Sans", 18, "bold"), fg="#8B0000", bg="white")
        self.level_label.place(relx=0.5, rely=0.1, anchor="center")

    def fetch_question(self, level):
        """Fetch a time question from the Clock Logic module."""
        question_bank = {
            1: "kvart över fem",
            2: "tio i tre",
            3: "halv sju"
        }
        return question_bank.get(level, "fem över åtta")

    def validate_answer(self, user_answer):
        """Validate the user's answer."""
        return user_answer.strip().lower() == self.correct_answer

    def provide_hint(self):
        """Fetch a hint from the Clock Logic module."""
        return "Think about 'över' and 'i'."
