# System modules
from tkinter import *
import pyglet
from os.path import join, dirname, normpath
from tkinter import messagebox
import json

# Integration modules
from sys import path as syspath
syspath.append(normpath(join(dirname(__file__), '../')))
from backend import user
from backend_module import backend_API
import ui

# CURRENT USER
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
theme = "Light"
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

# Localization
lang = 'en'
with open(normpath(join(root_dir, '..', 'loc', 'main_menu.json')), encoding="UTF-8") as f: loc = json.load(f)

# Main window
root = Tk()
root.title(loc[lang]["TITLE"])
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.state('zoomed')  

# Window size
root.geometry(f"{screen_width}x{screen_height}")
root.configure(background=THEMES[theme]["bg"])

def login_label():
    """Title on login page"""
    label_var = (StringVar(), "TITLE")
    label_var[0].set(loc[lang]["TITLE"])
    login_frame[0].stringvars.append(label_var)
    label = Label(login_frame[0], textvariable=label_var[0], font=(my_font, FONT_EXTRA_LARGE, "underline"), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])

    underlabel_var = (StringVar(), "TITLESUB")
    underlabel_var[0].set(loc[lang]["TITLESUB"])
    login_frame[0].stringvars.append(underlabel_var)
    underlabel = Label(login_frame[0], textvariable=underlabel_var[0], font=(my_font, FONT_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])

    label.place(relx=0.5, rely=0.15, anchor="center")
    underlabel.place(relx=0.5, rely=0.25, anchor="center")


def statistics_label():
    """Title on statistics page"""
    label_var = (StringVar(), "STATS")
    label_var[0].set(loc[lang]["STATS"])
    statistics_frame[0].stringvars.append(label_var)
    label = Label(statistics_frame[0], textvariable=label_var[0], font=(my_font, FONT_EXTRA_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])

    underlabel_var = (StringVar(), "STATS-LATEST")
    underlabel_var[0].set(loc[lang]["STATS-LATEST"])
    statistics_frame[0].stringvars.append(underlabel_var)
    underlabel = Label(statistics_frame[0], textvariable=underlabel_var[0], font=(my_font, FONT_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])

    label.place(relx=0.5, rely=0.10, anchor="center")
    underlabel.place(relx=0.5, rely=0.21, anchor="center")


def main_label():
    """Title on main page"""
    label_var = (StringVar(), "TITLE")
    label_var[0].set(loc[lang]["TITLE"])
    main_frame[0].stringvars.append(label_var)
    label = Label(main_frame[0], textvariable=label_var[0], font=(my_font, FONT_EXTRA_LARGE, "underline"), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])

    underlabel_var = (StringVar(), "TITLESUB")
    underlabel_var[0].set(loc[lang]["TITLESUB"])
    main_frame[0].stringvars.append(underlabel_var)
    underlabel = Label(main_frame[0], textvariable=underlabel_var[0], font=(my_font, FONT_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])

    label.place(relx=0.5, rely=0.15, anchor="center")
    underlabel.place(relx=0.5, rely=0.25, anchor="center")


def start_label():
    """Title on start page"""
    label_var = (StringVar(), "START-SEL")
    label_var[0].set(loc[lang]["START-SEL"])
    start_frame[0].stringvars.append(label_var)
    label = Label(start_frame[0], textvariable=label_var[0], font=(my_font, FONT_EXTRA_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    label.place(relx=0.5, rely=0.25, anchor="center")


def profile_label():
    """Title on start page"""
    label_var = (StringVar(), "USER")
    label_var[0].set(loc[lang]["USER"])
    profile_frame[0].stringvars.append(label_var)
    label = Label(profile_frame[0], textvariable=label_var[0], font=(my_font, FONT_LARGE), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    label.place(relx=0.5, rely=0.10, anchor="center")


# Tools
def round_rectangle(canvas, x1, y1, x2, y2, radius, **kwargs):
    """Round triangle buttons. This construction was taken from https://stackoverflow.com/a/44100075/15993687"""
    points = [x1+radius, y1, x1+radius, y1, x2-radius, y1, x2-radius, y1, x2, y1,
              x2, y1+radius, x2, y1+radius, x2, y2-radius, x2, y2-radius, x2, y2,
              x2-radius, y2, x2-radius, y2, x1+radius, y2, x1+radius, y2, x1, y2,
              x1, y2-radius, x1, y2-radius, x1, y1+radius, x1, y1+radius, x1, y1]
    return canvas.create_polygon(points, **kwargs, smooth=True)


def create_rounded_button(canvas, x, y, width, height, text, command, font, tag):
    """Create round button based on the round_rectangle() feature"""
    button = round_rectangle(canvas, x, y, x + width, y + height, radius=40, fill=THEMES[theme]["button"], outline=THEMES[theme]['button-h'], width=6)
    text_item = canvas.create_text((x + x+width) // 2, (y + y+height) // 2, text=text, font=font, fill=THEMES[theme]["text"], tags=tag)

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


def create_dropdown(canvas, x: int, y: int, options: list, stringvar: StringVar, command):
    dropdown = OptionMenu(canvas,
                          stringvar,
                          *options,
                          command=command)
    dropdown.config(width=18, height=1, font=(my_font, FONT_NORMAL, "bold"),
                    bg=THEMES[theme]['button'], fg=THEMES[theme]['text'],
                    activebackground=THEMES[theme]['button-h'],
                    activeforeground=THEMES[theme]['text-h'])
    dropdown.place(x=x,
                   y=y)
    return dropdown


def scale_font_size(val: str) -> None:
    def _set(mod: float):
        global font_scale

        old_font_scale = font_scale
        font_scale = mod
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

        for _frame in [main_frame[0], start_frame[0],
                       profile_frame[0], login_frame[0],
                       statistics_frame[0], accessibility_frame[0]]:
            for item in _frame.winfo_children():
                if isinstance(item, Label):
                    font = item.cget('font').split(" ")
                    font_size = int(((int(font[1]) / old_font_scale) * font_scale))

                    if len(font) == 3:  # Bold fonts
                        item.config(font=(font[0], font_size, font[2]))
                    elif len(font) == 2:    # Normal fonts
                        item.config(font=(font[0], font_size))
                    else:   # Error handling
                        item.config(font=(font[0], font_size))

    match val:
        case "50%": _set(0.5)
        case "75%": _set(0.75)
        case "100%": _set(1.0)
        case "125%": _set(1.25)
        case "150%": _set(1.5)


def set_theme(val: str) -> None:
    match val:
        case "Ljust": val = "Light"
        case "Mörkt": val = "Dark"

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


def set_language(val: str) -> None:
    global lang
    if lang == val: return
    lang = val

    # Frame labels
    for _frame in [main_frame[0], start_frame[0],
                   profile_frame[0], login_frame[0],
                   statistics_frame[0], accessibility_frame[0]]:
        for var in _frame.stringvars:
            var[0].set(loc[lang][var[1]])

    # Popup labels
    for var in root.stringvars:
        var[0].set(loc[lang][var[1]])

    # Text objects
    user_profile = user.get_user_profile()
    for _canvas in [main_frame[1], start_frame[1],
                    profile_frame[1], login_frame[1],
                    statistics_frame[1], accessibility_frame[1]]:
        _canvas.config(bg=THEMES[theme]['bg'])
        for item in _canvas.find_all():
            if _canvas.type(item) == 'text':
                _canvas.itemconfig(item, text=loc[lang][_canvas.itemcget(item, "tags").split(" ")[0]])
                match _canvas.itemcget(item, "tags").split(" ")[0]:     # Edge case for user profile
                    case "USER-NAME":
                        _canvas.itemconfig(item, text=f"{loc[lang]['USER-NAME']} {user_profile['first_name']} {user_profile['last_name']}")
                    case "USER-AGE":
                        _canvas.itemconfig(item, text=f"{loc[lang]['USER-AGE']} {user_profile['age']}")
                    case "USER-CNTR":
                        _canvas.itemconfig(item, text=f"{loc[lang]["USER-CNTR"]} {user_profile['country']}")

    # Theme dropdown
    accessibility_frame[0].theme_options = [loc[lang]["ACCESS-THEME-LIGHT"],
                                            loc[lang]["ACCESS-THEME-DARK"]]
    accessibility_frame[0].theme_setting = StringVar(root, accessibility_frame[0].theme_options[0]) if theme == "Light" else StringVar(root, accessibility_frame[0].theme_options[1])
    accessibility_frame[0].theme_dropdown.destroy()
    accessibility_frame[0].theme_dropdown = create_dropdown(accessibility_frame[1],
                                                            x=screen_width // 2 + 150, y=screen_height // 2 + 200,
                                                            options=accessibility_frame[0].theme_options,
                                                            stringvar=accessibility_frame[0].theme_setting,
                                                            command=lambda val: set_theme(val))


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
    def _close_clock_game(game_root: Toplevel, main_menu_root: Tk):
        game_root.destroy()
        main_menu_root.deiconify()

    clock_game_root = Toplevel()
    root.clock_game = ui.ClockGame(clock_game_root, return_to_main_menu_callback=lambda: _close_clock_game(clock_game_root, root))
    root.withdraw()
    clock_game_root.mainloop()


def on_placeholder_click():
    print("WILL BE IMPLEMENTED")


def on_match_the_words_click():
    print("WILL BE IMPLEMENTED")


def on_admin_control_click():
    print("WILL BE IMPLEMENTED")


def on_log_out_click():
    global current_user
    current_user = None
    main_frame[0].pack_forget()
    login_frame[0].pack(fill="both", expand=True)


def log_in_session() -> tuple[Frame, Canvas]:
    """Create main menu"""
    login_frame = Frame(root, bg=THEMES[theme]['bg'])
    login_frame.stringvars = []

    canvas = Canvas(login_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Round buttons with exact positions
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 200, 600, 200, loc[lang]["LOGIN"], on_login_click, (my_font, FONT_NORMAL), "LOGIN")
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 50, 600, 200, loc[lang]["NEWUSER"], on_register_click, (my_font, FONT_NORMAL), "NEWUSER")

    return (login_frame, canvas)


def on_login_click():
    """Pop-up window for user login"""
    popup = Toplevel(root)
    popup.title(loc[lang]["LOGIN-BTN"])
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
    login_username_label_var = (StringVar(), "LOGIN-USRN")
    login_username_label_var[0].set(loc[lang]["LOGIN-USRN"])
    root.stringvars.append(login_username_label_var)
    username_label = Label(popup, textvariable=login_username_label_var[0], font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    username_label.place(relx=0.5, rely=0.3, anchor="center")

    username_entry = Entry(popup, font=(my_font, FONT_SMALL), width=25)
    username_entry.place(relx=0.5, rely=0.4, anchor="center")
    username_entry.focus()

    # Login button inside the popup

    def login_user(even=None):
        #Fetch all information 
        global current_user, profile_frame, user_age, user_country, user_type, user_total_time, user_words_learned, user_fullname
        username = username_entry.get()
        
        user_profile = backend_API.get_user(username)  # Attempt to fetch user

        if not user_profile:
            #username_label.config(text=loc[lang]["LOGIN-ERR"], fg=THEMES[theme]['text'])
            messagebox.showerror("Login Failed", loc[lang]["LOGIN-ERR"])
            return  # Stop execution

        # Ensure required keys exist before accessing them
        user_fullname = user_profile.get("real_name", "Unknown")  # Default value if key is missing
        user_age = user_profile.get("age", "Unknown")
        user_country = user_profile.get("country", "Unknown")
        user_type = user_profile.get("user_type", "Unknown")
        user_total_time = user_profile.get("total_time", 0)
        user_words_learned = user_profile.get("words_learned", 0)

        if 'username' in user_profile and username == user_profile['username']:
            current_user = username
            popup.destroy()
            login_frame[0].pack_forget()
            main_frame[0].pack(fill="both", expand=True)

            profile_frame = profile_menu_table(current_user)
            profile_label()
        else:
            #username_label.config(text=loc[lang]["LOGIN-ERR"], fg=THEMES[theme]['text'])
            messagebox.showerror("Login Failed", loc[lang]["LOGIN-ERR"])

    login_btn = Button(popup, text=loc[lang]["LOGIN-BTN"], font=(my_font, FONT_SMALL), command=login_user, bg=THEMES[theme]['button'], fg=THEMES[theme]['text'])
    login_btn.place(relx=0.5, rely=0.55, anchor="center")

    popup.bind('<Return>', login_user)


def on_register_click():
    """Pop-up window for user register"""
    popup = Toplevel(root)
    popup.title(loc[lang]["NEWUSER-REG"])
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
    register_username_label_var = (StringVar(), "NEWUSER-USRN")
    register_username_label_var[0].set(loc[lang]["NEWUSER-USRN"])
    root.stringvars.append(register_username_label_var)
    username_label = Label(popup, textvariable=register_username_label_var[0], font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    username_label.place(relx=0.5, rely=0.06, anchor="center")
    username_entry = Entry(popup, font=(my_font, 14), width=25)
    username_entry.place(relx=0.5, rely=0.15, anchor="center")

    register_name_label_var = (StringVar(), "NEWUSER-NAME")
    register_name_label_var[0].set(loc[lang]["NEWUSER-NAME"])
    root.stringvars.append(register_name_label_var)
    name_label = Label(popup, textvariable=register_name_label_var[0], font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    name_label.place(relx=0.5, rely=0.22, anchor="center")
    name_entry = Entry(popup, font=(my_font, 14), width=25)
    name_entry.place(relx=0.5, rely=0.3, anchor="center")

    register_type_label_var = (StringVar(), "NEWUSER-TYPE")
    register_type_label_var[0].set(loc[lang]["NEWUSER-TYPE"])
    root.stringvars.append(register_type_label_var)
    usertype_label = Label(popup, textvariable=register_type_label_var[0], font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    usertype_label.place(relx=0.5, rely=0.37, anchor="center")
    usertype_entry = Entry(popup, font=(my_font, 14), width=25)
    usertype_entry.place(relx=0.5, rely=0.45, anchor="center")

    register_country_label_var = (StringVar(), "NEWUSER-CNTR")
    register_country_label_var[0].set(loc[lang]["NEWUSER-CNTR"])
    root.stringvars.append(register_country_label_var)
    country_label = Label(popup, textvariable=register_country_label_var[0], font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
    country_label.place(relx=0.5, rely=0.52, anchor="center")
    country_entry = Entry(popup, font=(my_font, 14), width=25)
    country_entry.place(relx=0.5, rely=0.6, anchor="center")

    register_age_label_var = (StringVar(), "NEWUSER-AGE")
    register_age_label_var[0].set(loc[lang]["NEWUSER-AGE"])
    root.stringvars.append(register_age_label_var)
    age_label = Label(popup, textvariable=register_age_label_var[0], font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg=THEMES[theme]['text'])
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
            # If age is not valid
            error_label = Label(popup, text="Invalid age. Please enter a valid number.", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg="red")
            error_label.place(relx=0.5, rely=0.9, anchor="center")
            return

        # Check if username already exist
        user_profile = backend_API.get_user(username)
        if user_profile:
            error_label = Label(popup, text="Username already taken. Please choose another.", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg="red")
            error_label.place(relx=0.5, rely=0.9, anchor="center")
            return
        backend_API.create_user(username, real_name=first_name, age=age, country=country, user_type=user_type)
        success_label = Label(popup, text="User registered successfully!", font=(my_font, FONT_SMALL), bg=THEMES[theme]['bg'], fg="green")
        success_label.place(relx=0.5, rely=0.9, anchor="center")
        popup.after(1000, popup.destroy)

    login_btn = Button(popup, text=loc[lang]["NEWUSER-REG"], font=(my_font, 12), command=register_user, bg=THEMES[theme]['button'], fg=THEMES[theme]['text'])
    login_btn.place(relx=0.5, rely=0.85, anchor="center")


def main_menu_table() -> tuple[Frame, Canvas]:
    """Create main menu"""
    menu_frame = Frame(root, bg=THEMES[theme]['bg'])
    menu_frame.stringvars = []

    canvas = Canvas(menu_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    # Round buttons with exact positions
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 200, 600, 75, loc[lang]["START"], on_start_click, (my_font, FONT_NORMAL), "START")
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 - 100, 600, 75, loc[lang]["USER"], on_user_profile_click, (my_font, FONT_NORMAL), "USER")
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 0, 600, 75, loc[lang]["STATS"], on_statistics_click, (my_font, FONT_NORMAL), "STATS")
    create_rounded_button(canvas, screen_width//2 - 300, screen_height//2 + 100, 600, 75, loc[lang]["ACCESS"], on_accessibility_click, (my_font, FONT_NORMAL), "ACCESS")

    create_rounded_button(canvas, screen_width - 160, screen_height - (screen_height - 60), 100, 50, loc[lang]["LOGOUT"], on_log_out_click, (my_font, FONT_SMALL), "LOGOUT")

    return (menu_frame, canvas)


def start_menu_table() -> tuple[Frame, Canvas]:
    """Create start menu"""
    start_frame = Frame(root, bg=THEMES[theme]['bg'])
    start_frame.stringvars = []

    canvas = Canvas(start_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Start menu buttons
    create_rounded_button(canvas, (screen_width - 250)//2 - 300, screen_height//2 - 200, 250, 250, loc[lang]["START-CLOCK"], on_clock_game_click, (my_font, FONT_NORMAL), "START-CLOCK")
    create_rounded_button(canvas, (screen_width - 250)//2, screen_height//2 - 200, 250, 250, loc[lang]["START-PAPER"], on_placeholder_click, (my_font, FONT_NORMAL), "START-PAPER")
    create_rounded_button(canvas, (screen_width - 250)//2 + 300, screen_height//2 - 200, 250, 250, loc[lang]["START-MATCH"], on_match_the_words_click, (my_font, FONT_NORMAL), "START-MATCH")

    # Go back button
    create_back_button(canvas, 15, 15)

    return (start_frame, canvas)


def profile_menu_table(current_user) -> tuple[Frame, Canvas]:
    """Profile page"""
    profile_frame = Frame(root, bg=THEMES[theme]['bg'])
    profile_frame.stringvars = []

    canvas = Canvas(profile_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Rectangle for user info
    round_rectangle(canvas, (screen_width - 500) // 2 - 200, (screen_height // 2) - 350, (screen_width - 500) // 2 + 700, (screen_height // 2) - 50, 20, fill=THEMES[theme]['button'], outline=THEMES[theme]['button-h'], width=4)

    # Add user icon - this can be replaced by the actual user image later
    user_icon_img = PhotoImage(file=join(images_dir, 'profile.png')).subsample(2)
    profile_frame.user_icon_img = user_icon_img
    canvas.profile_img = canvas.create_image((screen_width - 600) // 2 - 25, (screen_height // 2) - 205, image=user_icon_img, anchor="center", tags="profile")

    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 300,
                       text=f"{loc[lang]['USER-NAME']} {user_fullname}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'], tags="USER-NAME")

    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 250,
                       text=f"{loc[lang]['USER-CURR']} {current_user}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'], tags="USER-CURR")

    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 200,
                       text=f"{loc[lang]['USER-AGE']} {user_age}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'], tags="USER-AGE")

    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 150,
                       text=f"{loc[lang]['USER-CNTR']} {user_country}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'], tags="USER-CNTR")

    canvas.create_text((screen_width - 600) // 2 + 175, (screen_height // 2) - 100,
                       text=f"{loc[lang]['USER-TYPE']} {user_type}", font=(my_font, FONT_SMALL, "bold"), anchor="w", fill=THEMES[theme]['text'], tags="USER-TYPE")

    # Statistics and admin button
    create_rounded_button(canvas, (screen_width - 500) // 2 - 200, screen_height // 2, 900, 75, loc[lang]["USER-MYSTAT"], on_statistics_click, (my_font, FONT_NORMAL), "USER-MYSTAT")
    create_rounded_button(canvas, (screen_width - 500) // 2 - 200, screen_height // 2 + 100, 900, 75, loc[lang]["USER-ADMIN"], on_admin_control_click, (my_font, FONT_NORMAL), "USER-ADMIN")

    # Go back button
    create_back_button(canvas, 15, 15)

    return (profile_frame, canvas)

#Statistics page
def statistics_menu_table() -> tuple[Frame, Canvas]:
    """Create statistics page"""
    statistics_frame = Frame(root, bg=THEMES[theme]['bg'])
    statistics_frame.stringvars = []

    canvas = Canvas(statistics_frame, width=screen_width, height=screen_height, bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Statistics for first game
    round_rectangle(canvas, (screen_width - 1000) // 2, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 300, (screen_height - 500) // 2 + 250, 20, fill=THEMES[theme]['button'], outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 - 50, text=loc[lang]["STATS-TIME"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-TIME")
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 + 50, text=loc[lang]["STATS-CORR"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-CORR")
    canvas.create_text((screen_width - 1000) // 2 + 150, (screen_height - 250) // 2 + 150, text=loc[lang]["STATS-CLOCK"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-CLOCK")

    # Statistics for second game
    round_rectangle(canvas, (screen_width - 1000) // 2 + 350, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 650, (screen_height - 500) // 2 + 250, 20, fill=THEMES[theme]['button'], outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 - 50, text=loc[lang]["STATS-TIME"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-TIME")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 + 50, text=loc[lang]["STATS-MATCHED"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-MATCHED")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 250) // 2 + 150, text=loc[lang]["STATS-PAPER"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-PAPER")

    # Statistics for third game
    round_rectangle(canvas, (screen_width - 1000) // 2 + 700, (screen_height - 500) // 2, (screen_width - 1000) // 2 + 1000, (screen_height - 500) // 2 + 250, 20, fill=THEMES[theme]['button'], outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 - 50, text=loc[lang]["STATS-TIME"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-TIME")
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 + 50, text=loc[lang]["STATS-SOLVED"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-SOLVED")
    canvas.create_text((screen_width - 1000) // 2 + 850, (screen_height - 250) // 2 + 150, text=loc[lang]["STATS-MATCH"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-MATCH")

    # General statistics
    round_rectangle(canvas, (screen_width - 1000) // 2, (screen_height - 500) // 2 + 370, (screen_width - 1000) // 2 + 1000, (screen_height - 500) // 2 + 620, 20, fill=THEMES[theme]['button'], outline="darkred", width=4)
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 420, text=loc[lang]["STATS-LIFETIME"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-LIFETIME")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 470, text=loc[lang]["STATS-TOTALTIME"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-TOTALTIME")
    canvas.create_text((screen_width - 1000) // 2 + 500, (screen_height - 500) // 2 + 520, text=loc[lang]["STATS-LEARNED"], font=(my_font, FONT_SMALL, "bold"), anchor="center", fill=THEMES[theme]['text'], tags="STATS-LEARNED")

    # Go back button
    create_back_button(canvas, 15, 15)

    return statistics_frame, canvas


def accessibility_menu_table() -> tuple[Frame, Canvas]:
    """Initializes the accessibility page."""
    accessibility_frame = Frame(root, bg=THEMES[theme]['bg'])
    accessibility_frame.stringvars = []

    canvas = Canvas(accessibility_frame,
                    width=screen_width, height=screen_height,
                    bg=THEMES[theme]['bg'], highlightthickness=0)
    canvas.pack(expand=True, ipadx=50, ipady=50)

    # Settings
    center = {'x': screen_width // 2,
              'y': screen_height // 2}

    # Change language
    round_rectangle(canvas,
                    center['x'] - 700, center['y'] - 350,
                    center['x'] + 700, center['y'] - 50,
                    20, fill=THEMES[theme]['bg'], outline="darkred", width=4)
    canvas.create_text(center['x'], center['y'] - 300,
                       text=loc[lang]["ACCESS-CHANGE"], font=(my_font, FONT_LARGE, "bold"),
                       anchor="center", fill=THEMES[theme]['text'], tags="ACCESS-CHANGE")
    create_rounded_button(canvas,
                          center['x'] - 350, center['y'] - 250,
                          width=330, height=150,
                          text=loc[lang]["ACCESS-CHANGE-SE"], command=lambda: set_language("sv"),
                          font=(my_font, FONT_NORMAL),
                          tag="ACCESS-CHANGE-SE")
    create_rounded_button(canvas,
                          center['x'] + 20, center['y'] - 250,
                          width=330, height=150,
                          text=loc[lang]["ACCESS-CHANGE-EN"], command=lambda: set_language("en"),
                          font=(my_font, FONT_NORMAL),
                          tag="ACCESS-CHANGE-EN")

    # Resize font
    round_rectangle(canvas,
                    center['x'] - 700, center['y'] + 50,
                    center['x'] - 50, center['y'] + 350,
                    20, fill=THEMES[theme]['bg'], outline=THEMES[theme]['button-h'], width=4)
    canvas.create_text(center['x'] - 380, center['y'] + 100,
                       text=loc[lang]["ACCESS-RESIZE"], font=(my_font, FONT_LARGE, "bold"),
                       anchor="center", fill=THEMES[theme]['text'], tags="ACCESS-RESIZE")

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
    font_size_dropdown.place(x=center['x'] - 650,
                             y=center['y'] + 200)

    # Theme
    round_rectangle(canvas,
                    center['x'] + 50, center['y'] + 50,
                    center['x'] + 700, center['y'] + 350,
                    20, fill=THEMES[theme]['bg'], outline=THEMES[theme]['button-h'], width=4)
    canvas.create_text(center['x'] + 380, center['y'] + 100,
                       text=loc[lang]["ACCESS-THEME"], font=(my_font, FONT_LARGE, "bold"),
                       anchor="center", fill=THEMES[theme]['text'], tags="ACCESS-THEME")
    accessibility_frame.theme_options = [loc[lang]["ACCESS-THEME-LIGHT"],
                                         loc[lang]["ACCESS-THEME-DARK"]]
    accessibility_frame.theme_setting = StringVar(root, accessibility_frame.theme_options[0]) if theme == "Light" else StringVar(root, accessibility_frame.theme_options[1])
    accessibility_frame.theme_dropdown = create_dropdown(canvas, x=center['x'] + 150, y=center['y'] + 200,
                                                         options=accessibility_frame.theme_options, stringvar=accessibility_frame.theme_setting,
                                                         command=lambda val: set_theme(val))

    # Backwards navigation
    create_back_button(canvas, 15, 15)

    return (accessibility_frame, canvas)


# Create frames for different pages
main_frame = main_menu_table()
start_frame = start_menu_table()
# profile_frame = profile_menu_table(current_user)
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

# StringVars for root.
root.stringvars = []

# Safely quit if window is closed.
root.protocol("WM_DELETE_WINDOW", lambda: quit(0))

root.mainloop()
