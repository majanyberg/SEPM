from tkinter import Tk, messagebox, Button, Label, Frame
from WordSearch.array2d import Array2D


from WordSearch.apis.logic import Logic
from WordSearch.model.category import Category
from WordSearch.model.player import Player



class Application():
 
    def __init__(self):
          
        self.logic = Logic()
        self.num_hints = 3
        self.remaining_lives = 3
        self.category = Category.FOOD

        self.logic.init_player(self.num_hints, self.remaining_lives, self.category)

        self.word2DArray = self.logic.get_grid()

        self.selectedWords = ['CARROT', 'POTATO', 'FISH']
        self.found_words = []
        self.total_words = len(self.selectedWords)
        self.found_count = 0
        self.time_left = 600
        self.current_word = ""
        self.current_coords = []
        self.words_to_select_lbls = []

        self.build()

    def build(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title("Word Search")
        self.root.configure(bg='white')
        self.root.minsize(width=400, height=500)
        
        #Main UI group component
        control_panel = Frame(self.root, bg='white', pady=10)
        control_panel.grid(row=0, column=0, sticky='ew')        
        
        # Hint button: Need to add some command when we click on it
        #  TODO:
        hint_btn = Button(
            control_panel,
            text="HINT",
            font=('Arial', 12, 'bold'),
            bg='#4285F4',
            fg='white',
            border=0,
            padx=20,
            pady=5
        )
        hint_btn.grid(row=0, column=0, padx=10)


        #Displays found words.
        #Need to add a function that changes the color of the words when they are found.
        #TODO
        self.found_words_label = found_label = Label(
            control_panel,
            text=f"FOUND\n{self.found_count}/{self.total_words}",
            font=('Arial', 12, 'bold'),
            bg='#4285F4',
            fg='white',
            padx=20,
            pady=5
        )
        found_label.grid(row=0, column=1, padx=10)
        
        # Timer Label
        self.timer_label = Label(
            control_panel,
            text="08:42",
            font=('Arial', 16, 'bold'),
            bg='#FFD700',
            fg='black',
            padx=40,
            pady=5
        )
        self.timer_label.grid(row=0, column=2, padx=10)
        
        # Lives Label
        self.heart_labels = []  # Store references to heart labels
        lives_frame = Frame(control_panel, bg='#4285F4', padx=20, pady=5)
        lives_frame.grid(row=0, column=3, padx=10)
        for i in range(3):
            heart = Label(
                lives_frame,
                text="♥",
                font=('Arial', 14),
                fg='red' if i < self.remaining_lives else 'gray',
                bg='#4285F4'
            )
            heart.pack(side='left', padx=2)
            self.heart_labels.append(heart) 
        
        # Quit button
        quit_btn = Button(
            control_panel,
            text="QUIT",
            font=('Arial', 12, 'bold'),
            bg='#4285F4',
            fg='white',
            border=0,
            padx=20,
            pady=5,
            command=self.destroyGame
        )
        quit_btn.grid(row=0, column=4, padx=10)
        
        # Word search grid
        self.searchGrid = self.displayWordSearch()
        self.searchGrid.grid(row=1, column=0)
        
        # Words to find section with border
        self.words_frame = Frame(self.root, bg='white', pady=20)
        self.words_frame.grid(row=2, column=0)

        Label(
            self.words_frame,
            text="Words to select",
            font=('Arial', 20),
            fg="black",
            bg='white',
            pady=10
        ).pack()


        #Frame to hold the words to select
        bordered_frame = Frame(
            self.words_frame,
            bg='white',
            highlightbackground='black',
            highlightthickness=1,
            padx=20,
            pady=10
        )
        bordered_frame.pack(pady=10)

        word_list_frame = Frame(bordered_frame, bg='white', pady=10)
        word_list_frame.pack()

        for i, word in enumerate(self.selectedWords):
           self.words_to_select_lbls.append(Label(
                word_list_frame,
                text=word,
                font=('Arial', 12),
                fg="black",
                bg='white',
                padx=10
            ))
           self.words_to_select_lbls[i].grid(row=0, column=i)
           self.words_to_select_lbls[i].bind("<Button-1>", lambda l=self.words_to_select_lbls[i], w=word: self.check_word(l, w))
        
        self.update_timer()
        self.root.mainloop()

    def check_word(self, label, word):
        if self.logic.new_move(self.current_word, word):
            # if selected alphabets and the label matches
            struck_word = '\u0336'.join(word) + '\u0336'  # Add strikethrough
            label.config(text=struck_word, fg="gray")  # Change text and color
        else:
            # probably lose life
            self.resetSelection()
            return


    def displayWordSearch(self):
        self.WordSearchFrame = Frame(self.root, padx=20, pady=20)
        x = 20
        y = 20
        self.Buttons = Array2D(x, y)

        for i in range(x):
            for j in range(y):
                text = self.word2DArray[i][j]
                but = but =but = Button(
                    self.WordSearchFrame, 
                    text=text, 
                    width=2, 
                    height=1,
                    font=('Arial', 10),
                    bg='green',
                    fg='black',
                    disabledforeground='black', 
                    border=0,
                    command=lambda coords=(i, j): self.submitData(coords)
                )
                but.grid(row=i, column=j, padx=1, pady=1)
                self.Buttons[i, j] = but  

        return self.WordSearchFrame
    

    def udpate_found_words_label(self): #Refresh UI for found words
        self.found_words_label.configure(text=f"FOUND\n{self.found_count}/{self.total_words}")

    def update_lives_display(self): #Refresh Ui for lives display
        for i, heart in enumerate(self.heart_labels):
            heart.configure(fg='red' if i < self.remaining_lives else 'gray')
        
        if self.remaining_lives <= 0:
            self.destroyGame()
    


    # Function that buttons call on when they are clicked. When this is clicked I assume we communciate with logic layer and then get an updated state.
    # After doing that we update all UI elements that should be updated.
    # TODO 
    def submitData(self, coords):
        row, col = coords
        button = self.Buttons[row, col]  # Get the button correctly
        self.current_word += (button['text'])  # Append letter to the current word
        print("clicked for curr word: {}".format(self.current_word))
        self.current_coords.append([row, col])
        button.config(bg="orange", activebackground="orange", relief="solid", highlightbackground="orange")

    def resetSelection(self):
        """Reset the current word selection"""
        self.current_word = ""  # Clear the word
        self.current_coords = []


    #Endless loop that displays timer       
    def update_timer(self):
        if self.time_left > 0:
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.time_left -= 1
            self.found_words
            self.root.after(1000, self.update_timer)
        else:
            messagebox.showinfo("Time's up!", "Game Over!")
            self.destroyGame()
    
    def destroyGame(self):
        self.root.destroy()


def launch_puzzle_game():
    app = Application()
    

if __name__ == "__main__":
    launch_puzzle_game()

