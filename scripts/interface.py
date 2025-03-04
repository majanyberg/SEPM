from tkinter import *
import pyglet
from os.path import join, dirname, normpath
from tkinter import messagebox

from sys import path as syspath
syspath.append(normpath(join(dirname(__file__), '../')))
from backend import user
from integration_backend import backend_API

###CURRENT USER###
current_user = None 

# File paths
root_dir = dirname(__file__)
fonts_dir = normpath(join(root_dir, '..', 'fonts'))
images_dir = normpath(join(root_dir, '..', 'images'))

# Font
my_font = pyglet.font.add_file(join(fonts_dir, 'Work_Sans', 'WorkSans-Italic-VariableFont_wght.ttf'))
font_scale = float(1)
FONT_SMALL = int(12)
FONT_NORMAL = int(24)
FONT_LARGE = int(36)
FONT_EXTRA_LARGE = int(50)

# Themes
theme = "Dark"
THEMES = {
    "Light": {
        "bg": "#F0F0F0",
        "text": "#000000",
        "text-h": "#FFFFFF",
        "button": "#FFFFFF",
        "button-h": "#800000"
    },

    "Dark": {
        "bg": "#1F1F1F",
        "text": "#FFFFFF",
        "text-h": "#000000",
        "button": "#1F1F1F",
        "button-h": "#800000"
    }
}

# Main window
root = Tk()
root.title("Basic Swedish")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


# Window size
root.geometry(f"{screen_width}x{screen_height}")
root.configure(background=THEMES[theme]["bg"])


def login_label():
    """Title on login page"""
    label = Label(login_frame[0], text="Basic Swedish", font=(my_font, FONT_EXTRA_LARGE, "underline"), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    underlabel = Label(login_frame[0], text="Learn by playing", font=(my_font, FONT_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    label.place(relx=0.5, rely=0.15, anchor="center")
    underlabel.place(relx=0.5, rely=0.25, anchor="center")


def statistics_label():
    """Title on statistics page"""
    label = Label(statistics_frame[0], text="Statistics", font=(my_font, FONT_EXTRA_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    underlabel = Label(statistics_frame[0], text="Latest game session", font=(my_font, FONT_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    label.place(relx=0.5, rely=0.15, anchor="center")
    underlabel.place(relx=0.5, rely=0.21, anchor="center")


def main_label():
    """Title on main page"""
    label = Label(main_frame[0], text="Basic Swedish", font=(my_font, FONT_EXTRA_LARGE, "underline"), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    underlabel = Label(main_frame[0], text="Learn by playing", font=(my_font, FONT_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    label.place(relx=0.5, rely=0.15, anchor="center")
    underlabel.place(relx=0.5, rely=0.25, anchor="center")


def start_label():
    """Title on start page"""
    label = Label(start_frame[0], text="Select a game", font=(my_font, FONT_EXTRA_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    label.place(relx=0.5, rely=0.25, anchor="center")


def profile_label():
    """Title on start page"""
    label = Label(profile_frame[0], text="Current user", font=(my_font, FONT_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
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
    button = round_rectangle(canvas, x, y, x + width, y + height, radius=40, fill=THEMES[theme]["button"], outline=THEMES[theme]['button-h'], width=6)
    text_item = canvas.create_text((x + x+width) // 2, (y + y+height) // 2, text=text, font=font, fill=THEMES[theme]["text"])

    def on_hover(mouse):
        canvas.itemconfig(button, fill=THEMES[theme]["button-h"])
        canvas.itemconfig(text_item, fill=THEMES[theme]["text-h"])

    def off_hover(mouse):
        canvas.itemconfig(button, fill=THEMES[theme]["button"])
        canvas.itemconfig(text_item, fill=THEMES[theme]["text"])

    canvas.tag_bind(button, "<Enter>", on_hover)
    canvas.tag_bind(text_item, "<Enter>", on_hover)
    canvas.tag_bind(button, "<Leave>", off_hover)
    canvas.tag_bind(text_item, "<Leave>", off_hover)

    # Changes page when clicking on a button (+ text in the button)
    canvas.tag_bind(button, "<Button-1>", lambda event: command())  # Command() indicate the selected page function
    canvas.tag_bind(text_item, "<Button-1>", lambda event: command())

    return button, text_item


def scale_font_size(val: str) -> None:
    def _set(mod: float):
        global font_scale

        old_font_scale = font_scale
        font_scale = mod
        print(f"Old scale: {old_font_scale}\nNew scale: {font_scale}")
        for _canvas in [main_frame[1], start_frame[1],
                        profile_frame[1], login_frame[1],
                        statistics_frame[1], accessibility_frame[1]]:
            for item in _canvas.find_all():
                if _canvas.type(item) == 'text':
                    font = _canvas.itemcget(item, 'font').split()
                    font_size = int(((int(font[1]) / old_font_scale) * font_scale))

                    if len(font) == 3:  # Bold fonts
                        _canvas.itemconfig(item, font=(font[0], font_size, font[2]))
                    elif len(font) == 2:    # Normal fonts
                        _canvas.itemconfig(item, font=(font[0], font_size))
                    else:   # Error handling
                        _canvas.itemconfig(item, font=(font[0], font_size))

    match val:
        case "50%": _set(0.5)
        case "75%": _set(0.75)
        case "100%": _set(1.0)
        case "125%": _set(1.25)
        case "150%": _set(1.5)


def set_theme(val: str) -> None:
    global theme
    if theme == val: return
    theme = val

    root.configure(background=THEMES[theme]["bg"])

    # Change UU logo.
    # Messy because it's not part of any canvas.
    for e in [x for x in root.children.values() if isinstance(x, Label)]:
        e.destroy()
    root.uu_img = PhotoImage(
        file=join(images_dir, 'uu_logo_' + theme.lower() + '.png')
    ).subsample(4)  # 1/4th of original image size.
    root.uu_img_label = Label(root, image=root.uu_img, border=0)
    root.uu_img_label.place(relx=1, rely=1, anchor="se")
    root.uu_img.image = root.uu_img

    for _frame in [main_frame[0], start_frame[0],
                   profile_frame[0], login_frame[0],
                   statistics_frame[0], accessibility_frame[0]]:
        for item in _frame.winfo_children():
            if isinstance(item, Label):
                item.config(bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])

    for _canvas in [main_frame[1], start_frame[1],
                    profile_frame[1], login_frame[1],
                    statistics_frame[1], accessibility_frame[1]]:
        _canvas.config(bg=THEMES[theme]['bg'])
        for item in _canvas.find_all():
            match _canvas.type(item):
                case 'text':
                    _canvas.itemconfig(item, fill=THEMES[theme]['text'])
                case 'polygon':
                    _canvas.itemconfig(item, fill=THEMES[theme]['button'])
        for item in _canvas.winfo_children():
            if isinstance(item, OptionMenu):
                item.config(bg=THEMES[theme]['button'], fg=THEMES[theme]['text'],
                            activebackground=THEMES[theme]['button-h'],
                            activeforeground=THEMES[theme]['text-h'])


def create_back_button(master: Canvas, x: int, y: int):
    master.back_image = PhotoImage(
        file=join(images_dir, 'back.png')
    ).subsample(8)  # 1/8th of original image size.
    master.back_button = master.create_image(x, y, image=master.back_image, anchor="nw", tags="back")
    master.tag_bind(master.back_button, "<Button-1>", lambda event: go_main_page_click())
    master.back_image.image = master.back_image


# SWITCH BETWEEN PAGES
def on_start_click():
    """Switches to start page"""
    main_frame[0].pack_forget()
    start_frame[0].pack(fill="both", expand=True)


def go_main_page_click():
    """Switches to main page"""
    start_frame[0].pack_forget()
    profile_frame[0].pack_forget()
    statistics_frame[0].pack_forget()
    accessibility_frame[0].pack_forget()
    main_frame[0].pack(fill="both", expand=True)


def on_user_profile_click():
    main_frame[0].pack_forget()
    profile_frame[0].pack(fill="both", expand=True)


def on_statistics_click():
    main_frame[0].pack_forget()
    start_frame[0].pack_forget()
    profile_frame[0].pack_forget()
    statistics_frame[0].pack(fill="both", expand=True)


def on_accessibility_click():
    main_frame[0].pack_forget()
    start_frame[0].pack_forget()
    profile_frame[0].pack_forget()
    accessibility_frame[0].pack(fill="both", expand=True)


def on_clock_game_click():
    print("WILL BE IMPLEMENTED")


def on_placeholder_click():
    print("WILL BE IMPLEMENTED")


def on_match_the_words_click():
    print("WILL BE IMPLEMENTED")


def on_admin_control_click():
    print("WILL BE IMPLEMENTED")


def on_log_out_click():
    current_user = None 
    main_frame[0].pack_forget()
    login_frame[0].pack(fill="both", expand=True)


def log_in_session() -> tuple[Frame, Canvas]:
    """Create main menu"""
    login_frame = Frame(root, bg=THEMES[theme]['bg'])

    canvas = Canvas(login_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Round buttons with exact positions
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 200, 600, 200, "Login to session", on_login_click, (my_font, FONT_NORMAL))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 50, 600, 200, "Create a new user", on_register_click, (my_font, FONT_NORMAL))

    return (login_frame, canvas)


def on_login_click():
    """Pop-up window for user login"""
    popup = Toplevel(root)
    popup.title("Login")
    popup_width = 500
    popup_height = 400

    # Center the pop up window
    x_cordinate = int((screen_width / 2) - (popup_width / 2))
    y_cordinate = int((screen_height / 2) - (popup_height / 2))

    popup.geometry(f"{popup_width}x{popup_height}+{x_cordinate}+{y_cordinate}")
    popup.configure(bg=THEMES[theme]['bg'])
    popup.wait_visibility()
    popup.grab_set()  # Focus on popup window until closed

    # Username label and entry field
    username_label = Label(popup, text="Username:", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    username_label.place(relx=0.5, rely=0.3, anchor="center")
    username_entry = Entry(popup, font=(my_font, FONT_SMALL), width=25)
    username_entry.place(relx=0.5, rely=0.4, anchor="center")

    # Login button inside the popup
    def login_user():
        #Fetch all information 
        global current_user, profile_frame, user_age, user_country, user_type, user_total_time, user_words_learned, user_fullname
        username = username_entry.get()
        user_profile = backend_API.get_user(username) #Username
        user_fullname = backend_API.get_user(username)["real_name"] #Age of user
        user_age = backend_API.get_user(username)["age"] #Age of user
        user_country=backend_API.get_user(username)["country"] #Country 
        user_type= backend_API.get_user(username)["user_type"] #User type
        user_total_time = backend_API.get_user(username)["total_time"] #user total time stored
        user_words_learned = backend_API.get_user(username)["words_learned"] #user words learned stored 


        if user_profile and 'username' in user_profile and username == user_profile['username']:
            current_user = username  
            popup.destroy()
            login_frame[0].pack_forget()
            main_frame[0].pack(fill="both", expand=True)
            
            profile_frame = profile_menu_table(current_user)
            profile_label()
        else:
            username_label.config(text="Incorrect username:", fg=THEMES[theme]['text'])
    
    login_btn = Button(popup, text="Login", font=(my_font, FONT_SMALL), command=login_user, bg=THEMES[theme]['button-h'], fg=THEMES[theme]['text-h'])
    login_btn.place(relx=0.5, rely=0.55, anchor="center")

def on_register_click():
    """Pop-up window for user register"""
    popup = Toplevel(root)
    popup.title("Register")
    popup_width = 500
    popup_height = 450

    # Center the pop-up window
    x_cordinate = int((screen_width / 2) - (popup_width / 2))
    y_cordinate = int((screen_height / 2) - (popup_height / 2))

    popup.geometry(f"{popup_width}x{popup_height}+{x_cordinate}+{y_cordinate}")
    popup.configure(bg=THEMES[theme]['bg'])
    popup.wait_visibility()
    popup.grab_set()  # Focus on popup window until closed

    # Input fields
    username_label = Label(popup, text="Write a username:", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    username_label.place(relx=0.5, rely=0.06, anchor="center")
    username_entry = Entry(popup, font=(my_font, 14), width=25)
    username_entry.place(relx=0.5, rely=0.15, anchor="center")

    name_label = Label(popup, text="Write your name:", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    name_label.place(relx=0.5, rely=0.22, anchor="center")
    name_entry = Entry(popup, font=(my_font, 14), width=25)
    name_entry.place(relx=0.5, rely=0.3, anchor="center")

    usertype_label = Label(popup, text="Type of student:", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    usertype_label.place(relx=0.5, rely=0.37, anchor="center")
    usertype_entry = Entry(popup, font=(my_font, 14), width=25)
    usertype_entry.place(relx=0.5, rely=0.45, anchor="center")

    country_label = Label(popup, text="Write your country:", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    country_label.place(relx=0.5, rely=0.52, anchor="center")
    country_entry = Entry(popup, font=(my_font, 14), width=25)
    country_entry.place(relx=0.5, rely=0.6, anchor="center")

    age_label = Label(popup, text="Write your age:", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    age_label.place(relx=0.5, rely=0.67, anchor="center")
    age_entry = Entry(popup, font=(my_font, 14), width=25)
    age_entry.place(relx=0.5, rely=0.75, anchor="center")

    # Register button inside the popup
    def register_user():
        username = username_entry.get()
        first_name = name_entry.get()
        user_type = usertype_entry.get()
        country = country_entry.get()
        age = age_entry.get()

        if not username or not first_name or not user_type or not country or not age:
            error_label = Label(popup, text="All fields are required!", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg="red")
            error_label.place(relx=0.5, rely=0.9, anchor="center")
            return
        
        try:
            age = int(age)
        except ValueError:
            #If age is not valid
            error_label = Label(popup, text="Invalid age. Please enter a valid number.", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg="red")
            error_label.place(relx=0.5, rely=0.9, anchor="center")
            return

        #Check if username already exist
        user_profile = backend_API.get_user(username)
        if user_profile:
            error_label = Label(popup, text="Username already taken. Please choose another.", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg="red")
            error_label.place(relx=0.5, rely=0.9, anchor="center")
            return
        backend_API.create_user(username, real_name=first_name, age=age, country=country, user_type=user_type)
        success_label = Label(popup, text="User registered successfully!", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg="green")
        success_label.place(relx=0.5, rely=0.9, anchor="center")
        popup.after(1000, popup.destroy)  

    login_btn = Button(popup, text="Register", font=(my_font, 12), command=register_user, bg=THEMES[theme]['button-h'], fg=THEMES[theme]['text-h'])
    login_btn.place(relx=0.5, rely=0.85, anchor="center")


def main_menu_table() -> tuple[Frame, Canvas]:
    """Create main menu"""
    menu_frame = Frame(root, bg=THEMES[theme]['bg'])

    canvas = Canvas(menu_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Round buttons with exact positions
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 200, 600, 75, "Start", on_start_click, (my_font, FONT_NORMAL))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 100, 600, 75, "User Profile", on_user_profile_click, (my_font, FONT_NORMAL))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 0, 600, 75, "Statistics", on_statistics_click, (my_font, FONT_NORMAL))
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 100, 600, 75, "Accessibility", on_accessibility_click, (my_font, FONT_NORMAL))

    create_rounded_button(canvas, screen_width - 160, screen_height - (screen_height - 60), 100, 50, "Log out", on_log_out_click, (my_font, FONT_SMALL))

    return (menu_frame, canvas)


def start_menu_table() -> tuple[Frame, Canvas]:
    """Create start menu"""
    start_frame = Frame(root, bg=THEMES[theme]['bg'])

    canvas = Canvas(start_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Start menu buttons
    create_rounded_button(canvas, (screen_width - 250)//2 - 300, screen_height//2 - 200, 250, 250, "Clock Game", on_clock_game_click, (my_font, FONT_NORMAL))
    create_rounded_button(canvas, (screen_width - 250)//2, screen_height//2 - 200, 250, 250, "Placeholder", on_placeholder_click, (my_font, FONT_NORMAL))
    create_rounded_button(canvas, (screen_width - 250)//2 + 300, screen_height//2 - 200, 250, 250, "Match the words", on_match_the_words_click, (my_font, FONT_NORMAL))

    # Go back button
    create_back_button(canvas, 15, 15)

    return (start_frame, canvas)


def profile_menu_table(current_user) -> tuple[Frame, Canvas]:
    """Profile page"""
    profile_frame = Frame(root, bg=THEMES[theme]['bg'])

    canvas = Canvas(profile_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Rectangle for user info
    round_rectangle(canvas, (screen_width - 500) // 2 - 200, (screen_height // 2) - 350, (screen_width - 500) // 2 + 700, (screen_height // 2) - 50, 20, fill=THEMES[theme]['bg'], outline=THEMES[theme]['button-h'], width=4)

    # Add user icon - this can be replaced by the actual user image later
    user_icon_img = PhotoImage(file=join(images_dir, 'profile.png')).subsample(2)
    profile_frame.user_icon_img = user_icon_img
    canvas.profile_img = canvas.create_image((screen_width - 600) // 2 - 25, (screen_height // 2) - 205, image=user_icon_img, anchor="center", tags="profile")

    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 300,
                       text=f"Name: {user_fullname}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'])

    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 250,
                       text=f"Username: {current_user}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'])

    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 200,
                       text=f"Age: {user_age}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'])
    
    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 150,
                       text=f"Country: {user_country}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'])

    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 100,
                       text=f"Type of student: {user_type}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'])

    
    # Statistics and admin button
    create_rounded_button(canvas, (screen_width - 500) // 2 - 200, screen_height // 2, 900, 75, "My Statistics", on_statistics_click, (my_font, FONT_NORMAL))
    create_rounded_button(canvas, (screen_width - 500) // 2 - 200, screen_height // 2 + 100, 900, 75, "Admin Controls", on_admin_control_click, (my_font, FONT_NORMAL))

    # Go back button
    create_back_button(canvas, 15, 15)

    return (profile_frame, canvas)


def statistics_menu_table() -> tuple[Frame, Canvas]:
    """Create statistics page"""
    statistics_frame = Frame(root, bg=THEMES[theme]['bg'])

    canvas = Canvas(statistics_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Statistics for first game
    round_rectangle(canvas, (screen_width - 1000) // 2, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 300, (screen_height - 500) // 2 + 250, 20, fill=THEMES[theme]['bg'], outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 - 50, text="Time played:", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 + 50, text="Correct answers:", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 + 150, text="Clock game", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])

    # Statistics for second game
    round_rectangle(canvas, (screen_width - 1000) // 2 + 350, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 650, (screen_height - 500) // 2 + 250, 20, fill=THEMES[theme]['bg'], outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 - 50, text="Time played:", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 + 50, text="Matched items:", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 + 150, text="Furniture game", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])

    # Statistics for third game
    round_rectangle(canvas, (screen_width - 1000) // 2 + 700, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 1000, (screen_height - 500) // 2 + 250, 20, fill=THEMES[theme]['bg'], outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 - 50, text="Time played:", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 + 50, text="Puzzle solved:", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 + 150, text="Puzzle game", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])

    # General statistics
    round_rectangle(canvas, (screen_width - 1000) // 2, (screen_height - 500) // 2 + 370, (screen_width - 1000) // 2 + 1000, (screen_height - 500) // 2 + 620, 20, fill=THEMES[theme]['bg'], outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 420, text="Lifetime statistics:", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 470, text="Total time spent learning:", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 520, text="Words learned:", font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'])

    # Go back button
    create_back_button(canvas, 15, 15)

    return (statistics_frame, canvas)


def accessibility_menu_table() -> tuple[Frame, Canvas]:
    """Initializes the accessibility page."""
    accessibility_frame = Frame(root, bg=THEMES[theme]['bg'])

    canvas = Canvas(accessibility_frame,
                    width=screen_width, height=screen_height,
                    bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Settings
    DEBUG = 0
    center = {'x': screen_width // 2,
              'y': screen_height // 2}

    # Change language
    round_rectangle(canvas,
                    center['x'] - 700, center['y'] - 350,
                    center['x'] + 700, center['y'] - 50,
                    20, fill=THEMES[theme]['bg'], outline="darkred", width=4)
    canvas.create_text(center['x'], center['y'] - 300,
                       text="Change Language", font=(my_font, FONT_LARGE, "bold"),
                       anchor="center", fill=THEMES[theme]['text'])
    create_rounded_button(canvas,
                          center['x'] - 350, center['y'] - 250,
                          width=330, height=150,
                          text="Swedish", command="",
                          font=(my_font, FONT_NORMAL))
    create_rounded_button(canvas,
                          center['x'] + 20, center['y'] - 250,
                          width=330, height=150,
                          text="English", command="",
                          font=(my_font, FONT_NORMAL))

    # Resize font
    round_rectangle(canvas,
                    center['x'] - 700, center['y'] + 50,
                    center['x'] - 50, center['y'] + 350,
                    20, fill=THEMES[theme]['bg'], outline=THEMES[theme]['button-h'], width=4)
    canvas.create_text(center['x'] - 380, center['y'] + 100,
                       text="Resize Font", font=(my_font, FONT_LARGE, "bold"),
                       anchor="center", fill=THEMES[theme]['text'])

    font_size_options = ["50%", "75%", "100%", "125%", "150%"]
    font_size_setting = StringVar(root, "100%")
    font_size_dropdown = OptionMenu(canvas,
                                    font_size_setting,
                                    *font_size_options,
                                    command=lambda val: scale_font_size(val))
    font_size_dropdown.config(width=18, height=1, font=(my_font, FONT_NORMAL, "bold"),
                              bg=THEMES[theme]['button'], fg=THEMES[theme]['text'],
                              activebackground=THEMES[theme]['button-h'],
                              activeforeground=THEMES[theme]['text-h'])
    font_size_dropdown.place(x=center['x'] - 600,
                             y=center['y'] + 200)

    # Theme
    round_rectangle(canvas,
                    center['x'] + 50, center['y'] + 50,
                    center['x'] + 700, center['y'] + 350,
                    20, fill=THEMES[theme]['bg'], outline=THEMES[theme]['button-h'], width=4)
    canvas.create_text(center['x'] + 380, center['y'] + 100,
                       text="Theme", font=(my_font, FONT_LARGE, "bold"),
                       anchor="center", fill=THEMES[theme]['text'])
    theme_options = ["Light", "Dark"]
    theme_setting = StringVar(root, theme)
    theme_dropdown = OptionMenu(canvas,
                                theme_setting,
                                *theme_options,
                                command=lambda val: set_theme(val))
    theme_dropdown.config(width=18, height=1, font=(my_font, FONT_NORMAL, "bold"),
                          bg=THEMES[theme]['button'], fg=THEMES[theme]['text'],
                          activebackground=THEMES[theme]['button-h'],
                          activeforeground=THEMES[theme]['text-h'])
    theme_dropdown.place(x=center['x'] + 150,
                         y=center['y'] + 200)

    # Backwards navigation
    create_back_button(canvas, 15, 15)

    # DEBUG: CenterX, CenterY
    if DEBUG:
        round_rectangle(canvas,
                        center['x'] - 1, 0,
                        center['x'] + 1, screen_height,
                        1, fill='red', outline='red', width=1)
        round_rectangle(canvas,
                        0, center['y'] - 1,
                        screen_width, center['y'] + 1,
                        1, fill='red', outline='red', width=1)

    return (accessibility_frame, canvas)


# Create frames for different pages
main_frame = main_menu_table()
start_frame = start_menu_table()
#profile_frame = profile_menu_table(current_user)
login_frame = log_in_session()
statistics_frame = statistics_menu_table()
accessibility_frame = accessibility_menu_table()

# Call the titles for the different pages
main_label()
start_label()
login_label()
statistics_label()

# Show the main menu as default
login_frame[0].pack(fill="both", expand=True)

# Uppsala university logo
root.uu_img = PhotoImage(
    file=join(images_dir, 'uu_logo_' + theme.lower() + '.png')
).subsample(4)  # 1/4th of original image size.
root.uu_img_label = Label(root, image=root.uu_img, border=0)
root.uu_img_label.place(relx=1, rely=1, anchor="se")
root.uu_img.image = root.uu_img

root.mainloop()
