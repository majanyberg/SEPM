from tkinter import *
from tkinter import PhotoImage

#Main window
root = Tk()
root.title("Basic Swedish")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#UU icon for window - CHANGE WHEN TEACHER PROVIDES A BETTER ONE
root.wm_iconbitmap('images/UU_logo.ico')

#Window size according to computer width and height
root.geometry(f"{screen_width}x{screen_height}")
root.configure(background='#F0F0F0')

#Swedish class label
label = Label(root, text="Basic Swedish", font=("Arial", 50), bg="#F0F0F0", fg='#800000')
label.place(relx=0.5, rely=0.2, anchor="center")  

def menu_table(): 
    """"
    Inspo taken from: 
    https://www.geeksforgeeks.org/python-tkinter-frame-widget/ 
    https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
    https://www.tutorialspoint.com/python/tk_button.htm
    https://www.geeksforgeeks.org/python-creating-a-button-in-tkinter/

    ROUND BUTTON INSPO: https://stackoverflow.com/questions/42579927/how-to-make-a-rounded-button-tkinter
    https://www.youtube.com/watch?v=czaqpo_yZwk
    """
    menu_frame = Frame(root, bg='#F0F0F0') 
    
    first = Button(menu_frame, text="Start", width=30, height=1, bg='#800000', fg='#F0F0F0', relief="solid", borderwidth="0", font=("Arial", 15, 'bold'), padx=20, pady=20)
    first.grid(row=0, column=0, pady=10)

    second = Button(menu_frame, text="User Profile", width=30, height=1, bg='#800000', fg='#F0F0F0', relief="solid", borderwidth="0", font=("Arial", 15, 'bold'), padx=20, pady=20)
    second.grid(row=1, column=0, pady=10)

    third = Button(menu_frame, text="Statistics", width=30, height=1, bg='#800000', fg='#F0F0F0', relief="solid", borderwidth="0", font=("Arial", 15, 'bold'), padx=20, pady=20)
    third.grid(row=2, column=0, pady=10)

    fourth = Button(menu_frame, text="Accessibility", width=30, height=1, bg='#800000', fg='#F0F0F0', relief="solid", borderwidth="0", font=("Arial", 15, 'bold'), padx=20, pady=20)
    fourth.grid(row=3, column=0, pady=10)

    return menu_frame

#Get our menu table and place it in the middle
table = menu_table().place(relx=0.5, rely=0.5, anchor="center")  

#Uppsala University logo - WE NEED TO CHANGE IMAGE
image = PhotoImage(file="images/uupsala-400-height-1.png")

#Make image smaler
width = int(image.width() * 0.5)
height = int(image.height() * 0.5)
image = image.subsample(int(image.width() / width), int(image.height() / height))

#Add image to window
image_label = Label(root, image=image)
image_label.place(relx=1, rely=1, anchor="se")

root.mainloop()
