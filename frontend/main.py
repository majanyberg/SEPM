import tkinter as tk

from backend.main import getNouns, getHenID
from frontend.GameCanvas import GameCanvas

bgColor = "deepskyblue"

root = tk.Tk()
root.geometry("800x500")
root.title("Word Game!")
root.resizable(False, False)
root.configure(bg=bgColor)

label1 = tk.Label(root, bg=bgColor, fg="Black",text="Drag descriptions of dress items and Drop them where they belong!", font=("Arial Bold", 20))
label1.pack(pady=20)

gameCanvas = GameCanvas(root, 800, 440, bgColor)

henID = getHenID()
gameCanvas.createHen(henID)
gameCanvas.addWords(getNouns(henID))

gameCanvas.place(x=0, y=60)
root.mainloop()