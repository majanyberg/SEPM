import tkinter as tk

from backend.main import getNouns, getCharacter, getAdjectives
from backend.Character import Character
from frontend.GameCanvas import GameCanvas

class Application:
    
    def run(self):
        bgColor = "tan1"

        root = tk.Tk()
        root.geometry("1000x800")
        root.title("Word Game!")
        root.resizable(False, False)
        root.configure(bg=bgColor)

        gameCanvas = GameCanvas(root, 1000, 800, bgColor)

        character = getCharacter(1)
        gameCanvas.createCharacter(character)
        gameCanvas.addNouns(getNouns(character.getID()))
        gameCanvas.addAdjectives(getAdjectives(character.getID()))

        gameCanvas.place(x=0, y=0)
        root.mainloop()
