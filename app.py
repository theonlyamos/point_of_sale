from tkinter import *
from tkinter import ttk

from pages import LoginPage
from pages import MainLayoutPage

APP_NAME = "Supermarket Billing System"
APP_VERSION = '0.0.1'

supermarket_app = Tk()
supermarket_app.title(APP_NAME)
supermarket_app.geometry("400x200")
supermarket_app.overrideredirect(False)

login_page = LoginPage(supermarket_app)
mainlayout = MainLayoutPage(supermarket_app)

intro_frame = Frame(
    supermarket_app,
    width=400,
    height=200
)

def startup():
    global intro_frame
    global mainlayout

    intro_frame.place_forget()
    login_page.initialize()

loader = ttk.Progressbar(
    intro_frame,
    mode='determinate',
    length=200,
    maximum=100
)

loader.grid(column=0, row=0)

intro_frame.after(5, loader.start)

intro_frame.place(anchor='c', relx=0.5, rely=0.5)
intro_frame.after(500, startup)

supermarket_app.mainloop()


