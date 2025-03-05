import tkinter as tk

from backend.main import validateAnswer

class GameCanvas:

    wordPositions = {} # word: (x, y)
    descPositions = [] # (x, y, slotAvailable, wordOccupyingSlot)

    def __init__(self, root, width, height, bg):
        self.canvas = tk.Canvas(root, width=width, height=height, bg=bg, bd=0, highlightthickness=0)

    def addWords(self, words):
        spacing = 10
        x = 30
        y = 10
        for i, word in enumerate(words):
            self.createWord(word, x, y)
            self.wordPositions[word] = (x, y)

            bounds = self.canvas.bbox(word)
            itemWidth = bounds[2] - bounds[0]

            if x + itemWidth > 780:
                x = 30
                y += 50
                self.canvas.moveto(word, x, y)
                self.wordPositions[word] = (x, y)

            x += itemWidth + spacing

    # TODO: make henLines depend on henID
    def createHen(self, henID):
        global hen
        hen = tk.PhotoImage(file=f"frontend/assets/hen{henID}.png")
        self.canvas.create_image(20, 170, image=hen, anchor="nw")
        self.createHenLine(80, 200, 190, 195)
        self.createHenLine(107, 290, 215, 255)
        self.createHenLine(85, 343, 220, 315)
        self.createHenLine(100, 375, 215, 370)
        self.descPositions.append((190, 195, True, ""))
        self.descPositions.append((215, 255, True, ""))
        self.descPositions.append((220, 315, True, ""))
        self.descPositions.append((215, 370, True, ""))

    def createHenLine(self, x1, y1, x2, y2):
        lineWidth = 3
        lineColor = "white"
        self.canvas.create_line(x1, y1, x2, y2, width=lineWidth, fill=lineColor)
        self.canvas.create_oval(x1 - 3, y1 - 3, x1 + 3, y1 + 3, fill=lineColor)
        self.canvas.create_oval(x2 - 5, y2 - 5, x2 + 5, y2 + 5, fill=lineColor)
        self.canvas.create_oval(x2 - 9, y2 - 9, x2 + 9, y2 + 9, dash=(4, 4), width=1)

    def createWordBox(self, x, y, width, height, tag):
        boxColor = "gold"
        outlineColor = "white"
        radius = 20
        innerRadius = radius - 4
        outlineWidth = 3
        # Outline
        self.canvas.create_oval(x, y, x + radius, y + radius, fill=outlineColor, outline='', tags=tag) # nw corner circle
        self.canvas.create_oval(x, y + height - radius, x + radius, y + height, fill=outlineColor, outline='', tags=tag) # sw corner circle

        self.canvas.create_oval(x + width - radius, y, x + width, y + radius, fill=outlineColor, outline='', tags=tag) # ne corner circle
        self.canvas.create_oval(x + width - radius, y + height - radius, x + width, y + height, fill=outlineColor, outline='', tags=tag) # se corner circle

        self.canvas.create_rectangle(x, y + radius / 2, x + width, y + height - radius / 2, fill=outlineColor, outline='', tags=tag) # covers left to right
        self.canvas.create_rectangle(x + radius / 2, y, x + width - radius / 2, y + height, fill=outlineColor, outline='', tags=tag) # covers top to bottom
        # Inner box
        self.canvas.create_oval(x + outlineWidth, y + outlineWidth, x + innerRadius + outlineWidth, y + innerRadius + outlineWidth, fill=boxColor, outline='', tags=tag) # nw corner circle
        self.canvas.create_oval(x + outlineWidth, y + height - innerRadius - outlineWidth, x + innerRadius + outlineWidth, y + height - outlineWidth, fill=boxColor, outline='', tags=tag) # sw corner circle

        self.canvas.create_oval(x + width - innerRadius - outlineWidth, y + outlineWidth, x + width - outlineWidth, y + innerRadius + outlineWidth, fill=boxColor, outline='', tags=tag) # ne corner circle
        self.canvas.create_oval(x + width - innerRadius - outlineWidth, y + height - innerRadius - outlineWidth, x + width - outlineWidth, y + height - outlineWidth, fill=boxColor, outline='', tags=tag) # se corner circle

        self.canvas.create_rectangle(x + outlineWidth, y + innerRadius / 2 + outlineWidth, x + width - outlineWidth, y + height - innerRadius / 2 - outlineWidth, fill=boxColor, outline='', tags=tag) # covers left to right
        self.canvas.create_rectangle(x + innerRadius / 2 + outlineWidth, y + outlineWidth, x + width - innerRadius / 2 - outlineWidth, y + height - outlineWidth, fill=boxColor, outline='', tags=tag) # covers top to bottom

    def createWord(self, word, x, y):
        innerPadding = 10
        canvasText = self.canvas.create_text(x + innerPadding, y + innerPadding, text=word, fill="black", font='Arial 15 bold', anchor="nw", tags=word)

        bounds = self.canvas.bbox(canvasText)
        textWidth = bounds[2] - bounds[0]
        textHeight = bounds[3] - bounds[1]

        self.createWordBox(x, y, textWidth + innerPadding * 2, textHeight + innerPadding * 2, word)
        self.canvas.tag_raise(canvasText)
        self.createWordKeyBind(word)

    def moveWord(self, e, tag):
        bounds = self.canvas.bbox(tag)
        itemWidth = bounds[2] - bounds[0]
        itemHeight = bounds[3] - bounds[1]
        self.canvas.tag_raise(tag)
        self.canvas.moveto(tag, e.x - itemWidth/2, e.y - itemHeight/2)

    def snapWord(self, e, tag):
        self.canvas.moveto(tag, self.wordPositions[tag][0], self.wordPositions[tag][1])
        h = 60
        v = 30
        wordsInSlots = []
        for i, (x, y, b, t) in enumerate(self.descPositions):
            bounds = self.canvas.bbox(tag)

            if x - h < e.x < x + h and y - v < e.y < y + v and b:
                itemWidth = bounds[2] - bounds[0]
                itemHeight = bounds[3] - bounds[1]
                self.canvas.moveto(tag, x - itemWidth / 2, y - itemHeight / 2)

                # Resets boolean in other description position incase word occupied another slot before
                for k, (x2, y2, b2, t2) in enumerate(self.descPositions):
                    if b2 == False and t2 == tag:
                        self.descPositions[k] = (x2, y2, True, "")

                self.descPositions[i] = (x, y, False, tag)

            # Resets boolean to True when word is removed
            if b == False and (bounds[0], bounds[1]) == self.wordPositions[tag] and t == tag:
                self.descPositions[i] = (x, y, True, "")

            wordsInSlots.append(self.descPositions[i][3])

        if validateAnswer(wordsInSlots):
            self.win()

    def createWordKeyBind(self, tag):
        self.canvas.tag_bind(tag, "<B1-Motion>", lambda e: self.moveWord(e, tag))
        self.canvas.tag_bind(tag, "<ButtonRelease-1>", lambda e: self.snapWord(e, tag))

    def win(self):
        self.canvas.create_text(400, 190, text="Level cleared!", fill="green4", font='Arial 40 bold', anchor="center", tags="winText")

    def place(self, x, y):
        self.canvas.place(x=x, y=y)