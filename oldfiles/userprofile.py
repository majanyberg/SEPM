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
label = Label(root, text="Basic Swedish", font=("Work Sans", 50, "underline"), fg='black')
underlabel = Label(root, text="Learn by playing", font=("Work Sans", 30), fg='black')
label.place(relx=0.5, rely=0.15, anchor="center")  
underlabel.place(relx=0.5, rely=0.25, anchor="center")  

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
    button = round_rectangle(canvas, x, y, x + width, y + height, radius=40, fill="white", outline="#800000", width=3)
    text_item = canvas.create_text((x + x+width) // 2, (y + y+height) // 2, text=text, font=("Work Sans", 15, 'bold'), fill="black")
    
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
def on_start_click():
    print("WILL BE IMPEMENTED")

def on_user_profile_click():
    print("WILL BE IMPLEMENTED")

def on_statistics_click():
    print("WILL BE IMPLEMENTED")

def on_accessibility_click():
    print("WILL BE IMPLEMENTED")

def menu_table():
    """"
    Inspiration taken from: 
    https://www.geeksforgeeks.org/python-tkinter-frame-widget/ 
    https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
    https://www.tutorialspoint.com/python/tk_button.htm
    https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/
    https://www.geeksforgeeks.org/how-do-you-create-a-button-on-a-tkinter-canvas/
    
    ROUND BUTTON INSPO: https://stackoverflow.com/questions/42579927/how-to-make-a-rounded-button-tkinter
    https://www.youtube.com/watch?v=czaqpo_yZwk
    """
    menu_frame = Frame(root, bg='#F0F0F0')
    menu_frame.pack()

    canvas = Canvas(menu_frame, width=400, height=300, bg='#F0F0F0', highlightthickness=0)
    canvas.pack()

    # Create round buttons with references to the click commands, not function calls
    create_rounded_button(canvas, 50, 20, 300, 50, "Start", on_start_click)
    create_rounded_button(canvas, 50, 80, 300, 50, "User Profile", on_user_profile_click)
    create_rounded_button(canvas, 50, 140, 300, 50, "Statistics", on_statistics_click)
    create_rounded_button(canvas, 50, 200, 300, 50, "Accessibility", on_accessibility_click)

    return menu_frame

#Add menu in the middle of the menu
table = menu_table().place(relx=0.5, rely=0.5, anchor="center")

#Uppsala university logo
image = PhotoImage(file="images/uupsala-400-height-1.png")

#Scale image
width = int(image.width() * 0.5)
height = int(image.height() * 0.5)
image = image.subsample(int(image.width() / width), int(image.height() / height))

#Add image to window - CHANGE WHEN TEACHER PROVIDES A BETTER ONE
image_label = Label(root, image=image)
image_label.place(relx=1, rely=1, anchor="se")

root.mainloop()
