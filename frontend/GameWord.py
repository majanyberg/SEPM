from frontend.RoundedRectangle import RoundedRectangle

class GameWord:

    def __init__(self, word, canvas, x, y, bg, validateAnsFunc = None, winFunc = None, descPositions = None, inLevelMaker = False):
        self.word = word
        self.startX = x
        self.startY = y
        self.canvas = canvas
        self.bg = bg
        self.validateAnsFunc = validateAnsFunc
        self.winFunc = winFunc
        self.descPositions = descPositions
        self.inLevelMaker = inLevelMaker
        self.createWord(word, x, y)

    def createWord(self, word, x, y):
        innerPadding = 10
        canvasText = self.canvas.create_text(x + innerPadding, y + innerPadding, text=word, fill="black", font='Arial 15 bold', anchor="nw", tags=word)

        bounds = self.canvas.bbox(canvasText)
        textWidth = bounds[2] - bounds[0]
        textHeight = bounds[3] - bounds[1]

        self.createWordBox(x, y, textWidth + innerPadding * 2, textHeight + innerPadding * 2, word)
        self.canvas.tag_raise(canvasText)
        self.createWordKeyBind(word)

    def createWordBox(self, x, y, width, height, tag):
        RoundedRectangle(self.canvas, x, y, width, height, self.bg, tag)

    def moveWord(self, e, tag):
        bounds = self.canvas.bbox(tag)
        itemWidth = bounds[2] - bounds[0]
        itemHeight = bounds[3] - bounds[1]
        self.canvas.tag_raise(tag)
        self.canvas.moveto(tag, e.x - itemWidth/2, e.y - itemHeight/2)

    def snapWord(self, e, tag):
        self.canvas.moveto(tag, self.startX, self.startY)
        h = 60
        v = 30
        wordsInSlots = []
        for i, (x, y, isSlotAvailable, wordOccupyingSlot) in enumerate(self.descPositions):
            bounds = self.canvas.bbox(tag)

            if x - h < e.x < x + h and y - v < e.y < y + v and isSlotAvailable:
                itemWidth = bounds[2] - bounds[0]
                itemHeight = bounds[3] - bounds[1]
                self.canvas.moveto(tag, x - itemWidth / 2, y - itemHeight / 2)

                # Resets boolean in other description position incase word occupied another slot before
                for k, (x2, y2, b2, t2) in enumerate(self.descPositions):
                    if not b2 and t2 == tag:
                        self.descPositions[k] = (x2, y2, True, "")

                self.descPositions[i] = (x, y, False, tag)

            # Resets boolean to True when word is removed
            if not isSlotAvailable  and (bounds[0], bounds[1]) != (x, y) and wordOccupyingSlot == tag:
                self.descPositions[i] = (x, y, True, "")

        for (_, _, _, wordOccupyingSlot) in self.descPositions:
            wordsInSlots.append(wordOccupyingSlot)

        if self.validateAnsFunc(wordsInSlots):
            self.winFunc()

    def createWordKeyBind(self, tag):
        if not self.inLevelMaker:
            self.canvas.tag_bind(tag, "<B1-Motion>", lambda e: self.moveWord(e, tag))
            self.canvas.tag_bind(tag, "<ButtonRelease-1>", lambda e: self.snapWord(e, tag))

    def move(self, x, y):
        self.startX = x
        self.startY = y
        self.canvas.moveto(self.word, x, y)

