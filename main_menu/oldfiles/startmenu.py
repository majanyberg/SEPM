from tkinter import *
from tkinter import PhotoImage

#Main window
root = Tk()
root.title("Basic Swedish")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#UU icon for window
root.wm_iconbitmap('images/UU_logo.ico')

#Window size
root.geometry(f"{screen_width}x{screen_height}")
root.configure(background='#F0F0F0')

#Swedish class label
label = Label(root, text="Select a game", font=("Work Sans", 50), fg='black')
label.place(relx=0.5, rely=0.15, anchor="center")  


def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Round triangle buttons. This construction was taken from https://stackoverflow.com/a/44100075/15993687"""
    points = [x1+radius, y1,
              x1+radius, y1,
              x2-radius, y1,
              x2-radius, y1,
              x2, y1,
              x2, y1+radius,
              x2, y1+radius,
              x2, y2-radius,
              x2, y2-radius,
              x2, y2,
              x2-radius, y2,
              x2-radius, y2,
              x1+radius, y2,
              x1+radius, y2,
              x1, y2,
              x1, y2-radius,
              x1, y2-radius,
              x1, y1+radius,
              x1, y1+radius,
              x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def create_rounded_button(canvas, x, y, width, height, text, command):
    """Create round button based on the round_triangle() feature"""
    button = round_rectangle(canvas, x, y, x + width, y + height, radius=50, fill="white", outline="#800000", width=3)
    text_item = canvas.create_text((x + x+width) // 2, (y + y+height) // 2, text=text, font=("Work Sans", 20, 'bold'), fill="black")
    
    def on_hover(event):
        canvas.itemconfig(button, fill="#800000")  
        canvas.itemconfig(text_item, fill="white") 

    def off_hover(event):
        canvas.itemconfig(button, fill="white")  
        canvas.itemconfig(text_item, fill="black")  

    # Bind hover actions
    #https://www.geeksforgeeks.org/using-lambda-in-gui-programs-in-python/
    canvas.tag_bind(button, "<Enter>", on_hover)  
    canvas.tag_bind(button, "<Leave>", off_hover)  

    #Changes page when clickin on a button
    canvas.tag_bind(button, "<Button-1>", lambda event: command())
    
    return button, text_item


###COMMANDS FOR CHANGING PAGES###
#Changing page inspiration: https://www.geeksforgeeks.org/tkinter-application-to-switch-between-different-page-frames/
def on_clock_game_click():
    print("WILL BE IMPEMENTED")

def on_placeholder_click():
    print("WILL BE IMPLEMENTED")

def on_match_the_words_click():
    print("WILL BE IMPLEMENTED")

def menu_table():
    """"Menu with horizontally arranged buttons"""
    menu_frame = Frame(root, bg='#F0F0F0')
    menu_frame.pack()

    canvas = Canvas(menu_frame, width=750, height=150, bg='#F0F0F0', highlightthickness=0)
    canvas.pack(expand=True,ipadx=50, ipady=50)

    # Create 3 horizontal buttons
    create_rounded_button(canvas, 60, 10, 220, 150, "Clock Game", on_clock_game_click)
    create_rounded_button(canvas, 310, 10, 220, 150, "Placeholder", on_placeholder_click)
    create_rounded_button(canvas, 560, 10, 220, 150, "Match the words", on_match_the_words_click)

    return menu_frame

#Add menu in the middle of the menu
table = menu_table().place(relx=0.5, rely=0.5, anchor="center")


root.mainloop()
