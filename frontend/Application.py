import tkinter as tk
from tkinter import ttk

from backend.main import getNouns, getLevel, getAdjectives, getCharacter
from backend.Character import Character
from backend.Level import Level
from frontend.Game import Game
from frontend.LevelSelector import LevelSelector
from frontend.LevelMaker import LevelMaker

class Application:
    
    def run(self):
        self.bgColor = "tan1"

        self.root = tk.Tk()
        self.root.geometry("1000x800")
        self.root.title("Word Game!")
        self.root.resizable(False, False)
        self.root.configure(bg=self.bgColor)

        self.levelSelector = LevelSelector(self.root, self.startGame, self.startLevelMaker)
        self.levelSelector.createWidgets()

        self.root.mainloop()

    def startGame(self, levelName):
        self.levelSelector.destroy()

        game = Game(self.root, 1000, 800, self.bgColor)

        level = getLevel(levelName)
        game.addNouns(level.nouns)
        game.addAdjectives(level.adjectives)
        game.createCharacter(level.character)

        game.place(x=0, y=0)
    
    def startLevelMaker(self):
        self.levelSelector.destroy()

        levelMaker = LevelMaker(self.root, self.bgColor)
        levelMaker.createWidgets()

    
