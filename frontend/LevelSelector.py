
import tkinter as tk
from tkinter import ttk

from backend.main import levelExists
from backend.main import getLevelNames

class LevelSelector:

    def __init__(self, root, startGameFunc, startLevelMakerFunc):
        self.root = root
        self.startGameFunc = startGameFunc
        self.startLevelMakerFunc = startLevelMakerFunc

    def createWidgets(self):
        self.title = ttk.Label(master=self.root, text="Choose level in the dropdown menu!")
        self.title.pack(pady=20)

        levelNames = getLevelNames()
        self.levelDropdown = ttk.Combobox(master=self.root, values=levelNames)
        self.levelDropdown.pack()

        self.startLevelBtn = ttk.Button(master=self.root, text="Start", command=self.startGame)
        self.startLevelBtn.pack(pady=20)

        self.startLevelMakerBtn = ttk.Button(master=self.root, text="Level maker", command=self.startLevelMaker)
        self.startLevelMakerBtn.pack()
        
        self.errResponse = ttk.Label(master=self.root, text="")

    def startGame(self):
        if levelExists(self.levelDropdown.get()):
            self.startGameFunc(self.levelDropdown.get())
        else:
            self.errResponse.config(text="Failed to load level")
            self.errResponse.pack(pady=20)

    def startLevelMaker(self):
        self.startLevelMakerFunc()

    def destroy(self):
        self.title.destroy()
        self.levelDropdown.destroy()
        self.startLevelBtn.destroy()
        self.errResponse.destroy()
        self.startLevelMakerBtn.destroy()

