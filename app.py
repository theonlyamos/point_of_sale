from threading import Thread
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from connection_handler import ConnectionHandler
from PIL import ImageTk, Image
from time import sleep
import os

from pages import LoginPage
from pages import DashboardPage

from common import Database

APP_NAME = "Supermarket Billing System"
APP_VERSION = '0.0.1'

supermarket_app = Tk()
supermarket_app.title(APP_NAME)
supermarket_app.geometry("400x200")
supermarket_app.overrideredirect(False)

login_page = LoginPage(supermarket_app)
dashboad_page = DashboardPage(supermarket_app)

intro_frame = Frame(
    supermarket_app,
    width=400,
    height=200
)

def startup():
    global intro_frame
    global dashboad_page

    intro_frame.place_forget()
    login_page.initialize()

loader = ttk.Progressbar(
    intro_frame,
    mode='determinate',
    length=200,
    maximum=100
)

loader.grid(column=0, row=0)

intro_frame.after(50, loader.start)

intro_frame.place(anchor='c', relx=0.5, rely=0.5)
intro_frame.after(5000, dashboad_page.initialize())

supermarket_app.mainloop()


