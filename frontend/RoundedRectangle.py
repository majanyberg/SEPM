class RoundedRectangle:

    def __init__(self, canvas, x, y, width, height, backgroundColor, tag, outlineThiccness = 2, outerRadius = 10, innerRadius = 8, outlineColor = "white"):
        # Outline
        canvas.create_oval(x, y, x + outerRadius, y + outerRadius, fill=outlineColor, outline='', tags=tag) # nw corner circle
        canvas.create_oval(x, y + height - outerRadius, x + outerRadius, y + height, fill=outlineColor, outline='', tags=tag) # sw corner circle

        canvas.create_oval(x + width - outerRadius, y, x + width, y + outerRadius, fill=outlineColor, outline='', tags=tag) # ne corner circle
        canvas.create_oval(x + width - outerRadius, y + height - outerRadius, x + width, y + height, fill=outlineColor, outline='', tags=tag) # se corner circle

        canvas.create_rectangle(x, y + outerRadius / 2, x + width, y + height - outerRadius / 2, fill=outlineColor, outline='', tags=tag) # covers left to right
        canvas.create_rectangle(x + outerRadius / 2, y, x + width - outerRadius / 2, y + height, fill=outlineColor, outline='', tags=tag) # covers top to bottom
        # Inner box
        canvas.create_oval(x + outlineThiccness, y + outlineThiccness, x + innerRadius + outlineThiccness, y + innerRadius + outlineThiccness, fill=backgroundColor, outline='', tags=tag) # nw corner circle
        canvas.create_oval(x + outlineThiccness, y + height - innerRadius - outlineThiccness, x + innerRadius + outlineThiccness, y + height - outlineThiccness, fill=backgroundColor, outline='', tags=tag) # sw corner circle

        canvas.create_oval(x + width - innerRadius - outlineThiccness, y + outlineThiccness, x + width - outlineThiccness, y + innerRadius + outlineThiccness, fill=backgroundColor, outline='', tags=tag) # ne corner circle
        canvas.create_oval(x + width - innerRadius - outlineThiccness, y + height - innerRadius - outlineThiccness, x + width - outlineThiccness, y + height - outlineThiccness, fill=backgroundColor, outline='', tags=tag) # se corner circle

        canvas.create_rectangle(x + outlineThiccness, y + innerRadius / 2 + outlineThiccness, x + width - outlineThiccness, y + height - innerRadius / 2 - outlineThiccness, fill=backgroundColor, outline='', tags=tag) # covers left to right
        canvas.create_rectangle(x + innerRadius / 2 + outlineThiccness, y + outlineThiccness, x + width - innerRadius / 2 - outlineThiccness, y + height - outlineThiccness, fill=backgroundColor, outline='', tags=tag) # covers top to bottom