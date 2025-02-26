from tkinter import *
from tkinter.font import Font
from os.path import join, dirname, normpath

from sys import path as syspath
syspath.append(normpath(join(dirname(__file__), '../')))
from backend import user

user_profile = user.get_user_profile()
print(user_profile["first_name"])