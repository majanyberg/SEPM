import tkinter as tk

from backend.main import validateAnswer
from backend.Character import Character
from backend.ClothingItem import ClothingItem
from backend.Position import Position
from frontend.GameWord import GameWord
from frontend.RoundedRectangle import RoundedRectangle

# "Restart" and "Levels" button not fully implemented
class Game:

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
            gameWord = GameWord(word, self.canvas, x, y, bg, self.validateAnswerFunc, self.win, self.descPositions)
            self.words.append(gameWord)

            bounds = self.canvas.bbox(word)
            itemWidth = bounds[2] - bounds[0]

            if x + itemWidth > newLineThreshold:
                x = startX
                y += ySpacing
                gameWord.move(x, y)

            x += itemWidth + xSpacing

    def createCharacter(self, character):
        self.character = character
        global characterImg
        characterImg = tk.PhotoImage(file=character.path_to_img)
        characterImg = characterImg.subsample(5, 5)
        offsetX = 330
        offsetY = 330
        self.canvas.create_image(offsetX+20, offsetY+170, image=characterImg, anchor="nw")
        for clothingItem in character.clothes:
            centerPos = clothingItem.clothingPosition
            wordPos = clothingItem.wordPosition
            allWordPositions = self.calculateWordPositions(wordPos, clothingItem.name, clothingItem.adjectives)
            self.createWordLine(centerPos, allWordPositions, offsetX, offsetY)
            
            for wp in allWordPositions:
                self.descPositions.append((offsetX + wp.x, offsetY + wp.y, True, ""))


    def calculateWordPositions(self, firstWordPos, clothingName, adjectives):
        wordPositions = [firstWordPos]
        # for i, adjective in enumerate(adjectives):
        #     for gameWord in self.words:
        #         if adjective == gameWord.word:
        #             bounds = self.canvas.bbox(adjective)
        #             itemWidth = bounds[2] - bounds[0]
        #             wordPositions.append(Position(wordPositions[i].x + itemWidth / 2 + 30, wordPositions[i].y))
        spacing = 5
        for i in range(1, len(adjectives)):
            bounds = self.canvas.bbox(adjectives[i - 1])
            item1Width = bounds[2] - bounds[0]

            bounds = self.canvas.bbox(adjectives[i])
            item2Width = bounds[2] - bounds[0]
            wordPositions.append(Position(wordPositions[i - 1].x + item1Width / 2 + spacing + item2Width / 2, firstWordPos.y))
    
        bounds = self.canvas.bbox(adjectives[-1])
        item1Width = bounds[2] - bounds[0]

        bounds = self.canvas.bbox(clothingName)
        item2Width = bounds[2] - bounds[0]
        wordPositions.append(Position(wordPositions[-1].x + item1Width / 2 + spacing + item2Width / 2, firstWordPos.y))
    
        return wordPositions

    def createWordLine(self, clothingPosition, wordPositions, offsetX, offsetY):
        lineWidth = 3
        lineColor = "white"
        # Line from clothing item to first word
        self.canvas.create_line(offsetX + clothingPosition.x, offsetY + clothingPosition.y, offsetX + wordPositions[0].x, offsetY + wordPositions[0].y, width=lineWidth, fill=lineColor)
        self.canvas.create_oval(offsetX + clothingPosition.x - 3, offsetY + clothingPosition.y - 3, offsetX + clothingPosition.x + 3, offsetY + clothingPosition.y + 3, fill=lineColor)
        # Circle at words
        for wordPosition in wordPositions:
            self.canvas.create_oval(offsetX + wordPosition.x - 5, offsetY + wordPosition.y - 5, offsetX + wordPosition.x + 5, offsetY + wordPosition.y + 5, fill=lineColor)
            self.canvas.create_oval(offsetX + wordPosition.x - 9, offsetY + wordPosition.y - 9, offsetX + wordPosition.x + 9, offsetY + wordPosition.y + 9, dash=(4, 4), width=1)
            
        # Line between the words
        self.canvas.create_line(offsetX + wordPositions[0].x, offsetY + wordPositions[0].y, offsetX + wordPositions[-1].x, offsetY + wordPositions[-1].y, width=lineWidth, fill=lineColor)


    def validateAnswerFunc(self, choosenWords):
        if validateAnswer(self.character, choosenWords):
            self.win()

    def win(self):
        self.canvas.create_text(400, 190, text="Level cleared!", fill="green4", font='Arial 40 bold', anchor="center", tags="winText")

    def place(self, x, y):
        self.canvas.place(x=x, y=y)