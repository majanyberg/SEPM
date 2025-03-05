""" Required Functions from Clock Logic Module
Function	                                    Purpose
fetch_question(level: int) -> str	            Retrieves a time-related question based on difficulty level.
validate_answer(user_answer: str) -> bool	    Checks if the user's answer is correct.
provide_hint() -> str	                        Returns a hint for the current question.
start_level(root, level, back_to_menu_callback)	Manages the UI and logic for each level."""

import random
import tkinter as tk
from source.fetchQA.FetchQA import fetch_qa_temp # fetch a question and answer from a database
from source.state.Score import Score
from source.state.State import GameState
from source.level.Level import UserLevelManager
from tkinter import messagebox

class GameLogicConnector:
    def __init__(self):
        self.level_manager = UserLevelManager()

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
        question_data = fetch_qa_temp(f"level_{level}")
        self.correct_answer = question_data['answer']
        return question_data['question']

    def validate_answer(self, user_answer):
        """Validate the user's answer."""
        return user_answer.strip().lower() == self.correct_answer.strip().lower()

    def provide_hint(self):
        """Fetch a hint from the Clock Logic module."""
        return "Think about 'över' and 'i'."

    def fetch_score(self):
        """Fetch the current score from the backend."""
        score_instance = Score()
        return score_instance.get_score()

    def submit_answer(self, user_answer):
        """Submit the user's answer."""
        if self.validate_answer(user_answer):
            GameState.correct_answer()
            return True, self.fetch_score()
        else:
            GameState.wrong_answer()
            return False, self.fetch_score()

    def update_level(self, score):
        """Update the user level based on their score."""
        return self.level_manager.update_level(score)

    def show_error_message(self, error_message):
        messagebox.showerror("Error", error_message)
