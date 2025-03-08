import tkinter as tk

from backend.main import validateAnswer
from backend.Character import Character
from backend.ClothingItem import ClothingItem
from backend.Position import Position
from frontend.GameWord import GameWord
from frontend.RoundedRectangle import RoundedRectangle

class GameCanvas:

    words = [] #
    descPositions = [] # (x, y, isSlotAvailable, wordOccupyingSlot)

    def __init__(self, root, width, height, bg):
        self.canvas = tk.Canvas(root, width=width, height=height, bg=bg, bd=0, highlightthickness=0)
        self.createWordContainer()
        self.createLevelsButton()
        self.createRestartButton()

    def createWordContainer(self):
        RoundedRectangle(self.canvas, 30, 30, 840, 400, "bisque", "wc", 6, 42, 34)
        RoundedRectangle(self.canvas, 30, 30, 175, 50, "white", "wtc", 6, 42, 34)
        self.canvas.create_text(50, 43, text="Paper Pelle", fill="black", font='Arial 25 bold', anchor="nw")
        self.canvas.create_text(220, 48, text="Drag descriptions of dress items and Drop them where they belong!", fill="black", font='Arial 19 bold', anchor="nw")

    def createLevelsButton(self):
        RoundedRectangle(self.canvas, 900, 30, 70, 70, "bisque", "menuBtn", 4, 30, 26)
        self.canvas.create_text(901, 103, text="Levels", fill="white", font='Arial 22 bold', anchor="nw")
        global lvlImg
        lvlImg = tk.PhotoImage(file="frontend/assets/three-stars.png")
        lvlImg = lvlImg.subsample(4, 4)
        self.canvas.create_image(902, 32, image=lvlImg, anchor="nw", tag="lvlImg")

    def createRestartButton(self):
        RoundedRectangle(self.canvas, 900, 150, 70, 70, "bisque", "menuBtn", 4, 30, 26)
        self.canvas.create_text(897, 223, text="Restart", fill="white", font='Arial 22 bold', anchor="nw")
        global restartImg
        restartImg = tk.PhotoImage(file="frontend/assets/restart.png")
        restartImg = restartImg.subsample(4, 4)
        self.canvas.create_image(912, 160, image=restartImg, anchor="nw", tag="restartImg")
        self.canvas.tag_raise("restartImg")

    def addNouns(self, words):
        self.canvas.create_text(70, 105, text="Nouns", fill="dark orange", font='Arial 22 bold', anchor="nw")
        self.createWords(words, 170, 100, "dark orange")
        
    def addAdjectives(self, words):
        self.canvas.create_text(50, 100+50*3 + 15, text="Adjectives", fill="DarkGoldenrod1", font='Arial 22 bold', anchor="nw")
        self.createWords(words, 170, 100+50*3 + 10, "DarkGoldenrod1")

    def createWords(self, words, x, y, bg):
        xSpacing = 10
        ySpacing = 50
        startX = x
        newLineThreshold = 850
        
        for word in words:
            gameWord = GameWord(word, self.canvas, x, y, bg, validateAnswer, self.win, self.descPositions)
            self.words.append(gameWord)

            bounds = self.canvas.bbox(word)
            itemWidth = bounds[2] - bounds[0]

            if x + itemWidth > newLineThreshold:
                x = startX
                y += ySpacing
                gameWord.move(x, y)

            x += itemWidth + xSpacing

    def createCharacter(self, character):
        global characterImg
        characterImg = tk.PhotoImage(file=character.getPath())
        offsetX = 380
        offsetY = 330
        self.canvas.create_image(offsetX+20, offsetY+170, image=characterImg, anchor="nw")
        for clothingItem in character.getClothes():
            self.createWordLine(clothingItem.getCenterPosition(), clothingItem.getWordPosition(), offsetX, offsetY)
        self.descPositions.append((offsetX+190, offsetY+195, True, ""))
        self.descPositions.append((offsetX+215, offsetY+255, True, ""))
        self.descPositions.append((offsetX+220, offsetY+315, True, ""))
        self.descPositions.append((offsetX+215, offsetY+370, True, ""))

    def createWordLine(self, p1, p2, offsetX, offsetY):
        p1.move(offsetX + p1.getX(), offsetY + p1.getY())
        p2.move(offsetX + p2.getX(), offsetY + p2.getY())
        lineWidth = 3
        lineColor = "white"
        self.canvas.create_line(p1.getX(), p1.getY(), p2.getX(), p2.getY(), width=lineWidth, fill=lineColor)
        self.canvas.create_oval(p1.getX() - 3, p1.getY() - 3, p1.getX() + 3, p1.getY() + 3, fill=lineColor)
        self.canvas.create_oval(p2.getX() - 5, p2.getY() - 5, p2.getX() + 5, p2.getY() + 5, fill=lineColor)
        self.canvas.create_oval(p2.getX() - 9, p2.getY() - 9, p2.getX() + 9, p2.getY() + 9, dash=(4, 4), width=1)

    def win(self):
        self.canvas.create_text(400, 190, text="Level cleared!", fill="green4", font='Arial 40 bold', anchor="center", tags="winText")

    def place(self, x, y):
        self.canvas.place(x=x, y=y)