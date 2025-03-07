import tkinter as tk
from tkinter import font as tkFont
from tkinter import messagebox
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
        self.create_option_buttons()
        self.load_question()

    def create_level_frame(self):
        self.level_frame = tk.Frame(self.root, bg="white")
        self.level_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def create_home_button(self):
        home_button = tk.Button(
            self.level_frame,
            text="🏠",
            font=self.font,
            bg="#8B0000",
            fg="white",
            relief="ridge",
            bd=3,
            command=self.back_to_menu_callback
        )
        home_button.place(relx=0.95, rely=0.05, anchor="center")

    def create_score_label(self):
        self.score_label = tk.Label(
            self.level_frame,
            text=f"Score: {self.score}",
            font=self.font,
            fg="#8B0000",
            bg="white"
        )
        self.score_label.place(relx=0.1, rely=0.05, anchor="w")

    def create_clock_label(self):
        if os.path.isfile(self.clock_image_path):
            self.clock_image = tk.PhotoImage(file=self.clock_image_path)
            self.clock_label = tk.Label(
                self.level_frame,
                image=self.clock_image,
                bg="white"
            )
            self.clock_label.place(relx=0.75, rely=0.4, anchor="center")
        else:
            self.clock_label = tk.Label(
                self.level_frame,
                text="(No Clock Image Found)",
                font=("Arial", 14),
                fg="red",
                bg="white"
            )
            self.clock_label.place(relx=0.75, rely=0.4, anchor="center")

    def create_question_label(self):
        self.question_label = tk.Label(
            self.level_frame,
            text="",
            font=("Arial", 28),
            fg="#8B0000",
            bg="white"
        )
        self.question_label.place(relx=0.75, rely=0.7, anchor="center")

    def create_option_buttons(self):
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(
                self.level_frame,
                text="",
                font=self.font,
                bg="gray",
                fg="white",
                relief="ridge",
                bd=3,
                command=lambda i=i: self.check_answer(i)
            )
            button.place(relx=0.3, rely=0.3 + i * 0.15, anchor="center", width=300, height=50)
            self.option_buttons.append(button)

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
                self.clock_label.image = self.clock_image  # Keep a reference to prevent garbage collection
            else:
                print("Error loading image from URL.")
            
            options = question_data.get("options", ["No options available"])
            self.game_logic.correct_answer = question_data["ans"]
            options.append(self.game_logic.correct_answer)
            random.shuffle(options)
            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option, bg="gray")
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
        if new_level <= self.level:
            self.load_question()
        else:
            self.show_level_complete_message(new_level)

    def show_level_complete_message(self, new_level):
        messagebox.showinfo(
            "Level Complete",
            f"Congratulations! You've completed Level {self.level}.\nYour score: {self.score}"
        )
        self.level = new_level
        self.game_logic.end_game()
        # self.load_question()

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Level 2 UI Test")
#     root.geometry("1080x720")
#     app = Level2UI(root, lambda: print("Back to menu"))
#     root.mainloop()

