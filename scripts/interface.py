from tkinter import *
from tkinter.font import Font 
import pyglet
from os.path import join, dirname, normpath

from sys import path as syspath
syspath.append(normpath(join(dirname(__file__), '../')))
from backend import user

# File paths
root = dirname(__file__)
fonts_dir = normpath(join(root, '..', 'fonts'))
images_dir = normpath(join(root, '..', 'images'))

# Font
my_font = pyglet.font.add_file(join(fonts_dir, 'Work_Sans', 'WorkSans-Italic-VariableFont_wght.ttf'))

# Main window
root = Tk()
root.title("Basic Swedish")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# UU icon for window
root.wm_iconbitmap('images/UU_logo.ico')

# Window size
root.geometry(f"{screen_width}x{screen_height}")
root.configure(background='#F0F0F0')

def login_label():
    """Title on login page"""
    label = Label(login_frame, text="Basic Swedish", font=(my_font, 50, "underline"), bg='#F0F0F0', fg='black')
    underlabel = Label(login_frame, text="Learn by playing", font=(my_font, 30), bg='#F0F0F0', fg='black')
    label.place(relx=0.5, rely=0.15, anchor="center")  
    underlabel.place(relx=0.5, rely=0.25, anchor="center")  

def statistics_label():
    """Title on statistics page"""
    label = Label(statistics_frame, text="Statistics", font=(my_font, 50), bg='#F0F0F0', fg='black')
    underlabel = Label(statistics_frame, text="Latest game session", font=(my_font, 30), bg='#F0F0F0', fg='black')
    label.place(relx=0.5, rely=0.15, anchor="center")  
    underlabel.place(relx=0.5, rely=0.21, anchor="center")

def main_label():
    """Title on main page"""
    label = Label(main_frame, text="Basic Swedish", font=(my_font, 50, "underline"), bg='#F0F0F0', fg='black')
    underlabel = Label(main_frame, text="Learn by playing", font=(my_font, 30), bg='#F0F0F0', fg='black')
    label.place(relx=0.5, rely=0.15, anchor="center")  
    underlabel.place(relx=0.5, rely=0.25, anchor="center")  

def start_label():
    """Title on start page"""
    label = Label(start_frame, text="Select a game", font=(my_font, 50), bg='#F0F0F0', fg='black')
    label.place(relx=0.5, rely=0.25, anchor="center")  

def profile_label():
    """Title on start page"""
    label = Label(profile_frame, text="Current user", font=(my_font, 40), bg='#F0F0F0', fg='black')
    label.place(relx=0.5, rely=0.10, anchor="center")  

def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Round triangle buttons. This construction was taken from https://stackoverflow.com/a/44100075/15993687"""
    points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1,
              x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2, 
              x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2, 
              x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)

def create_rounded_button(canvas, x, y, width, height, text, command, font):
    """Create round button based on the round_rectangle() feature"""
    button = round_rectangle(canvas, x, y, x + width, y + height, radius=40, fill="white", outline="#800000", width=6)
    text_item = canvas.create_text((x + x+width) // 2, (y + y+height) // 2, text=text, font=font, fill="black")
    
    def on_hover(mouse):
        canvas.itemconfig(button, fill="#800000")  
        canvas.itemconfig(text_item, fill="white") 

    def off_hover(mouse):
        canvas.itemconfig(button, fill="white")  
        canvas.itemconfig(text_item, fill="black")  

    canvas.tag_bind(button, "<Enter>", on_hover)  
    canvas.tag_bind(button, "<Leave>", off_hover)  

    #Changes page when clicking on a button (+ text in the button)
    canvas.tag_bind(button, "<Button-1>", lambda event: command()) #Command() indicate the selected page function 
    canvas.tag_bind(text_item, "<Button-1>", lambda event: command())

    return button, text_item

# SWITCH BETWEEN PAGES
def on_start_click():
    """Switches to start page"""
    main_frame.pack_forget()
    start_frame.pack(fill="both", expand=True)

def go_main_page_click():
    """Switches to main page"""
    start_frame.pack_forget()
    profile_frame.pack_forget()
    statistics_frame.pack_forget()
    main_frame.pack(fill="both", expand=True)

def on_user_profile_click():
    main_frame.pack_forget()
    profile_frame.pack(fill="both", expand=True)

def on_statistics_click():
    print("WILL BE IMPLEMENTED")
    main_frame.pack_forget()
    start_frame.pack_forget()
    profile_frame.pack_forget()
    statistics_frame.pack(fill="both", expand=True)
    stats = user.get_user_stats()

def on_accessibility_click():
    print("WILL BE IMPLEMENTED")

def on_clock_game_click():
    print("WILL BE IMPLEMENTED")

def on_placeholder_click():
    print("WILL BE IMPLEMENTED")

def on_match_the_words_click():
    print("WILL BE IMPLEMENTED")

def on_admin_control_click():
    print("WILL BE IMPLEMENTED")

def on_log_out_click():
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def log_in_session():
    """Create main menu"""
    login_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(login_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")  

    #Round buttons with exact positions
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 200, 600, 200, "Login to session", on_login_click, (my_font, 15))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 50, 600, 200, "Create a new user", on_register_click, (my_font, 15))

    return login_frame

def on_login_click():
    """Pop-up window for user login"""
    popup = Toplevel(root)
    popup.title("Login")
    popup_width = 500
    popup_height = 400

    #Center the pop up window
    x_cordinate = int((screen_width / 2) - (popup_width / 2))
    y_cordinate = int((screen_height / 2) - (popup_height / 2))

    popup.geometry(f"{popup_width}x{popup_height}+{x_cordinate}+{y_cordinate}")
    popup.configure(bg='#F0F0F0')
    popup.wait_visibility()
    popup.grab_set()  #Focus on popup window until closed

    #Username label and entry field
    username_label = Label(popup, text="Username:", font=(my_font, 16), bg='#F0F0F0')
    username_label.place(relx=0.5, rely=0.3, anchor="center")
    username_entry = Entry(popup, font=(my_font, 14), width=25)
    username_entry.place(relx=0.5, rely=0.4, anchor="center")

    #Login button inside the popup
    def login_user():
        user_profile = user.get_user_profile()
        username = username_entry.get()
        if username == user_profile['username']:  
            popup.destroy()
            login_frame.pack_forget()
            main_frame.pack(fill="both", expand=True)

        else:
            username_label.config(text="Incorrect username:", fg="#800000")

    login_btn = Button(popup, text="Login", font=(my_font, 14), command=login_user, bg="#800000", fg="white")
    login_btn.place(relx=0.5, rely=0.55, anchor="center")


def on_register_click():
    """Pop-up window for user register"""
    popup = Toplevel(root)
    popup.title("Register")
    popup_width = 500
    popup_height = 450  

    #Center the pop-up window
    x_cordinate = int((screen_width / 2) - (popup_width / 2))
    y_cordinate = int((screen_height / 2) - (popup_height / 2))

    popup.geometry(f"{popup_width}x{popup_height}+{x_cordinate}+{y_cordinate}")
    popup.configure(bg='#F0F0F0')
    popup.wait_visibility()
    popup.grab_set()  #Focus on popup window until closed

    #Input fields
    username_label = Label(popup, text="Write a username:", font=(my_font, 10))
    username_label.place(relx=0.5, rely=0.06, anchor="center")  
    username_entry = Entry(popup, font=(my_font, 14), width=25)
    username_entry.place(relx=0.5, rely=0.15, anchor="center")  

    name_label = Label(popup, text="Write your name:", font=(my_font, 10))  
    name_label.place(relx=0.5, rely=0.22, anchor="center")  
    name_entry = Entry(popup, font=(my_font, 14), width=25)
    name_entry.place(relx=0.5, rely=0.3, anchor="center")  

    surname_label = Label(popup, text="Write your surname:", font=(my_font, 10))  
    surname_label.place(relx=0.5, rely=0.37, anchor="center")  
    surname_entry = Entry(popup, font=(my_font, 14), width=25)
    surname_entry.place(relx=0.5, rely=0.45, anchor="center")  

    country_label = Label(popup, text="Write your country:", font=(my_font, 10))  
    country_label.place(relx=0.5, rely=0.52, anchor="center")  
    country_entry = Entry(popup, font=(my_font, 14), width=25)
    country_entry.place(relx=0.5, rely=0.6, anchor="center")  

    age_label = Label(popup, text="Write your age:", font=(my_font, 10)) 
    age_label.place(relx=0.5, rely=0.67, anchor="center") 
    age_entry = Entry(popup, font=(my_font, 14), width=25)
    age_entry.place(relx=0.5, rely=0.75, anchor="center")  

    #Register button inside the popup
    def register_user():
        # IMPLEMENT IN THE INTEGRATION
        username = username_entry.get()
        first_name = name_entry.get()
        last_name = surname_entry.get()
        country = country_entry.get()
        age = age_entry.get()

        # Creating a profile for the new user
        user_profile_data = {
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "country": country,
            "age": int(age) 
        }

        user.add_user_profile(user_profile_data)
        popup.destroy()
    login_btn = Button(popup, text="Register", font=(my_font, 12), command=register_user, bg="#800000", fg="white")
    login_btn.place(relx=0.5, rely=0.85, anchor="center")

def main_menu_table():
    """Create main menu"""
    menu_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(menu_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")  

    #Round buttons with exact positions
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 200, 600, 75, "Start", on_start_click, (my_font, 15))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 100, 600, 75, "User Profile", on_user_profile_click, (my_font, 15))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 0, 600, 75, "Statistics", on_statistics_click, (my_font, 15))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 100, 600, 75, "Accessibility", on_accessibility_click, (my_font, 15))

    create_rounded_button(canvas, screen_width - 160, screen_height - (screen_height - 60), 100, 50, "Log out", on_log_out_click, (my_font, 10))

    return menu_frame


def start_menu_table():
    """Create start menu"""
    start_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(start_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    #Start menu buttons
    create_rounded_button(canvas, (screen_width - 250)//2 - 300, screen_height//2 - 200, 250, 250, "Clock Game", on_clock_game_click, (my_font, 15))
    create_rounded_button(canvas, (screen_width - 250)//2, screen_height//2 - 200, 250, 250, "Placeholder", on_placeholder_click, (my_font,15))
    create_rounded_button(canvas, (screen_width - 250)//2 + 300, screen_height//2 - 200, 250, 250, "Match the words", on_match_the_words_click, (my_font,15))

    #Go back button
    create_rounded_button(canvas, screen_width - (screen_width-60), screen_height - (screen_height - 60), 100, 50, "Go back", go_main_page_click, (my_font, 10))

    return start_frame


def profile_menu_table():
    """Profile page"""
    profile_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(profile_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Rectangle for user info
    round_rectangle(canvas, (screen_width - 500) // 2 - 200, (screen_height // 2) - 350, (screen_width - 500) // 2 + 700, (screen_height // 2) - 50, 20, fill="white", outline="darkred", width=4)

    # Add user icon - this can be replaced by the actual user image later
    user_icon_img = PhotoImage(file=join(images_dir, 'profile_logo.png'))
    # Resize image
    width = int(user_icon_img.width() * 0.4)
    height = int(user_icon_img.height() * 0.4)
    user_icon_img = user_icon_img.subsample(int(user_icon_img.width() / width), int(user_icon_img.height() / height))
    profile_frame.user_icon_img = user_icon_img
    canvas.create_image((screen_width - 600) // 2 - 25, (screen_height // 2) - 205, image=user_icon_img, anchor="center")
    user_profile = user.get_user_profile()
    # User information
    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 300,
                       text=f"Name: {user_profile['first_name']} {user_profile['last_name']}", font=(my_font, 16, "bold"), anchor="w", fill="black")
    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 250,
                       text=f"Age: {user_profile['age']}", font=(my_font, 16, "bold"), anchor="w", fill="black")
    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 200,
                       text=f"Country: {user_profile['country']}", font=(my_font, 16, "bold"), anchor="w", fill="black")

    # Statistics and admin button
    create_rounded_button(canvas, (screen_width - 500) // 2 - 200, screen_height // 2, 900, 75, "My Statistics", on_statistics_click, (my_font, 15))
    create_rounded_button(canvas, (screen_width - 500) // 2 - 200, screen_height // 2 + 100, 900, 75, "Admin Controls", on_admin_control_click, (my_font, 15))

    # Go back button
    create_rounded_button(canvas, screen_width - (screen_width-100), screen_height - (screen_height - 100), 100, 50, "Go back", go_main_page_click, (my_font, 10))

    return profile_frame

def statistics_menu_table():
    """Create statistics page"""
    statistics_frame = Frame(root, bg='#F0F0F0')

    canvas = Canvas(statistics_frame, width=screen_width, height=screen_height, bg='#F0F0F0', highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    #Statistics for first game
    round_rectangle(canvas, (screen_width - 1000) // 2, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 300, (screen_height - 500) // 2 + 250, 20, fill="white", outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 - 50, text="Time played:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 + 50, text="Correct answers:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 + 150, text="Clock game", font=(my_font, 14, "bold"), anchor="center", fill="black")

    #Statistics for second game
    round_rectangle(canvas, (screen_width - 1000) // 2 + 350, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 650, (screen_height - 500) // 2 + 250, 20, fill="white", outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 - 50, text="Time played:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 + 50, text="Matched items:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 + 150, text="Furniture game", font=(my_font, 14, "bold"), anchor="center", fill="black")

    #Statistics for third game
    round_rectangle(canvas, (screen_width - 1000) // 2 + 700, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 1000, (screen_height - 500) // 2 + 250, 20, fill="white", outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 - 50, text="Time played:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 + 50, text="Puzzle solved:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 + 150, text="Puzzle game", font=(my_font, 14, "bold"), anchor="center", fill="black")

    #General statistics
    round_rectangle(canvas, (screen_width - 1000) // 2, (screen_height - 500) // 2 + 370, (screen_width - 1000) // 2 + 1000, (screen_height - 500) // 2 + 620, 20, fill="white", outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 420, text="Lifetime statistics:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 470, text="Total time spent learning:", font=(my_font, 16, "bold"), anchor="center", fill="black")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 520, text="Words learned:", font=(my_font, 16, "bold"), anchor="center", fill="black")

    #Go back button
    create_rounded_button(canvas, screen_width - (screen_width - 60), screen_height - (screen_height - 60), 100, 50, "Go back", go_main_page_click, (my_font, 10))

    return statistics_frame

# Create frames for different pages
main_frame = main_menu_table()  
start_frame = start_menu_table() 
profile_frame = profile_menu_table()
login_frame = log_in_session()
statistics_frame = statistics_menu_table()

# Call the titles for the different pages
main_label()
start_label()
profile_label()
login_label()
statistics_label()

# Show the main menu as default
login_frame.pack(fill="both", expand=True)

# Uppsala university logo
image = PhotoImage(file=join(images_dir, 'uupsala-400-height-1.png'))

# Scale image
width = int(image.width() * 0.5)
height = int(image.height() * 0.5)
image = image.subsample(int(image.width() / width), int(image.height() / height))

# Add image to window - CHANGE WHEN TEACHER PROVIDES A BETTER ONE
image_label = Label(root, image=image, bg='#F0F0F0')
image_label.place(relx=1, rely=1, anchor="se")

root.mainloop()
