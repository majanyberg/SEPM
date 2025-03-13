import tkinter as tk
from tkinter import ttk

from backend.Character import Character
from backend.ClothingItem import ClothingItem
from backend.Position import Position
from backend.main import getCharacterPaths
from frontend.GameWord import GameWord
from frontend.RoundedRectangle import RoundedRectangle

# Very buggy, not yet done
class LevelMaker:

    words = [] #
    placingCircleOnClothing = False
    clothingPositions = []
    wordPositions = []
    wordPositionTags = []
    tagCounter = 0
    currentTag = ""
    undoList = []

    def __init__(self, root, bg):
        self.root = root
        self.canvas = tk.Canvas(root, width=1000, height=300, bg=bg, bd=0, highlightthickness=0)
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.place(x=0, y=500)

    def createWidgets(self):
        title = ttk.Label(master=self.root, text="Choose character")
        title.place(x=52, y=20)
        characterPaths = getCharacterPaths()
        self.characterDropdown = ttk.Combobox(master=self.root, values=characterPaths)
        self.characterDropdown.place(x=3, y=43)
        self.selectCharacterBtn = ttk.Button(master=self.root, text="Select", command=self.selectCharacter)
        self.selectCharacterBtn.place(x=60, y=74)

        levelNameLabel = ttk.Label(master=self.root, text="Level name")
        levelNameLabel.place(x=65, y=123)
        self.levelNameEntry = ttk.Entry(master=self.root)
        self.levelNameEntry.place(x=7, y=146)

        nounsLabel = ttk.Label(master=self.root, text="Nouns (one word per line)")
        nounsLabel.place(x=280, y=20)
        self.nounsText = tk.Text(master=self.root, height=25, width=27, highlightthickness=0)
        self.nounsText.place(x=280, y=40)

        adjectivesLabel = ttk.Label(master=self.root, text="Adjectives (one word per line)")
        adjectivesLabel.place(x=520, y=20)
        self.adjectivesText = tk.Text(master=self.root, height=25, width=27, highlightthickness=0)
        self.adjectivesText.place(x=520, y=40)

        characterWordLabel = ttk.Label(master=self.root, text="Add word to character")
        characterWordLabel.place(x=798, y=123)
        self.characterWordEntry = ttk.Entry(master=self.root)
        self.characterWordEntry.place(x=770, y=146)
        self.characterNextWordBtn = ttk.Button(master=self.root, text="Next word", command=self.nextWord)
        self.characterNextWordBtn.place(x=817, y=175)

        self.undoCircleBtn = ttk.Button(master=self.root, text="Undo circle", command=self.undoCircle)
        self.undoCircleBtn.place(x=880, y=465)

    def selectCharacter(self):
        if hasattr(self, 'imageID'):
            self.canvas.delete(self.imageID)
        if self.characterDropdown.get() in getCharacterPaths():
            self.createCharacter(self.characterDropdown.get())

    def createCharacter(self, characterFileName):
        global characterImg
        characterImg = tk.PhotoImage(file=f"characters/{characterFileName}")
        characterImg = characterImg.subsample(5, 5)
        self.imageID = self.canvas.create_image(300, 0, image=characterImg, anchor="nw")
        self.canvas.tag_lower(self.imageID)

    def on_click(self, e):
        self.placingCircleOnClothing = not self.placingCircleOnClothing
        pos = Position(e.x, e.y)
        if self.placingCircleOnClothing:
            self.addClothingCircle(pos)
        else:
            self.addWordCircle(pos)

    def addClothingCircle(self, pos):
        circleID = self.canvas.create_oval(pos.x - 3, pos.y - 3, pos.x + 3, pos.y + 3, fill="white")
        self.clothingPositions.append((pos, circleID))
    
    def addWordCircle(self, pos):
        spacing = 100
        line1ID = self.canvas.create_line(self.clothingPositions[-1][0].x, self.clothingPositions[-1][0].y, pos.x, pos.y, width=3, fill="white")
        line2ID = self.canvas.create_line(pos.x, pos.y, pos.x + spacing * 2, pos.y, width=3, fill="white")

        tag = self.createTag()
        inner1ID = self.canvas.create_oval(pos.x - 5, pos.y - 5, pos.x + 5, pos.y + 5, fill="white", tags=tag)
        outer1ID = self.canvas.create_oval(pos.x - 9, pos.y - 9, pos.x + 9, pos.y + 9, dash=(4, 4), width=1, tags=f"{tag}o")
        
        if self.currentTag == tag:
            self.canvas.itemconfig(tag, fill="black", outline="black")
            self.canvas.itemconfig(f"{tag}o", outline="black")

        pos.move(pos.x + spacing, pos.y)
        tag = self.createTag()
        inner2ID = self.canvas.create_oval(pos.x - 5, pos.y - 5, pos.x + 5, pos.y + 5, fill="white", tags=tag)
        outer2ID = self.canvas.create_oval(pos.x - 9, pos.y - 9, pos.x + 9, pos.y + 9, dash=(4, 4), width=1, tags=f"{tag}o")
        
        pos.move(pos.x + spacing, pos.y)
        tag = self.createTag()
        inner3ID = self.canvas.create_oval(pos.x - 5, pos.y - 5, pos.x + 5, pos.y + 5, fill="white", tags=tag)
        outer3ID = self.canvas.create_oval(pos.x - 9, pos.y - 9, pos.x + 9, pos.y + 9, dash=(4, 4), width=1, tags=f"{tag}o")

        self.undoList.append((line1ID, line2ID, inner1ID, outer1ID, inner2ID, outer2ID, inner3ID, outer3ID))

    def createTag(self):
        tag = f"wc{self.tagCounter}"
        self.wordPositionTags.append(tag)
        self.tagCounter += 1
        if self.currentTag == "":
            self.currentTag = tag
        return tag

    def undoCircle(self):
        if self.placingCircleOnClothing:
            if len(self.clothingPositions) != 0:
                element = self.clothingPositions.pop()
                if len(element) != 0:
                    self.canvas.delete(element[1])
        else:
            if len(self.clothingPositions) != 0:
                ids = self.undoList.pop()
                if len(ids) != 0:
                    for id in ids:
                        self.canvas.delete(id)
        
        self.placingCircleOnClothing = not self.placingCircleOnClothing

    def nextWord(self):
        if self.characterWordEntry.get():
            circleBounds = self.canvas.bbox(self.currentTag)
            circleWidth = circleBounds[2] - circleBounds[0]
            circleCenterX = circleBounds[2] - circleWidth / 2
            circleCenterY = circleBounds[3] - circleWidth / 2

            self.canvas.delete(self.characterWordEntry.get())

            gameWord = GameWord(self.characterWordEntry.get(), self.canvas, 0, 0, "DarkGoldenrod1", inLevelMaker=True)
            bounds = self.canvas.bbox(self.characterWordEntry.get())
            width = bounds[2] - bounds[0]
            height = bounds[3] - bounds[1]
            gameWord.move(circleCenterX - width / 2, circleCenterY - height / 2)

        index = self.wordPositionTags.index(self.currentTag)

        self.canvas.itemconfig(self.currentTag, fill="white", outline="white")
        self.canvas.itemconfig(f"{self.currentTag}o", outline="white")
        
        if index + 1 > len(self.wordPositionTags) - 1:
            self.currentTag = self.wordPositionTags[0]
        else:
            self.currentTag = self.wordPositionTags[index + 1]

        self.canvas.itemconfig(self.currentTag, fill="black", outline="black")
        self.canvas.itemconfig(f"{self.currentTag}o", outline="black")

    def testText(self):
        print(self.nounsText.get("1.0",'end-1c').splitlines())