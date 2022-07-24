from tkinter import *
from tkinter import ttk

from .dashboard import DashboardPage

class LoginPage():
    '''
    Login Page
    '''

    def __init__(self, window):
        self.window = window
        #self.initialize()
    
    def initialize(self):
        '''
        Initialize Page Contents
        '''

        self.window.geometry("400x450")
        self.window.title('LOGIN - Supermarket Billing System')
        self.frame = Frame(
            self.window,
            width=400,
            height=450
        )

        self.create_content()
        self.frame.place(anchor="c", relx=0.5, rely=0.5)
    
    def create_content(self):
        '''
        Create Login Page Components
        '''
        
        ttk.Label(
            self.frame,
            text='Login Page',
            font='Helvetica 20 bold',
            foreground='#da1039'
        ).place(anchor='c', relx=0.5, rely=0.15)
        
        ttk.Label(
            self.frame,
            text='Login As',
            font='sans-serif 11',
            foreground="#242424"
        ).place(anchor='c', relx=0.5, rely=0.3)

        role_var = StringVar()
        role_select = ttk.Combobox(
            self.frame,
            textvariable=role_var,
            font='monospace 10',
            foreground='#4e4e4e',
            background='white',
            values=('cashier', 'admin'),
            state='readonly'
        ).place(anchor='c', width=250, height=35, relx=0.5, rely=0.36)

        ttk.Label(
            self.frame,
            text='Email Address',
            font='sans-serif 11',
            foreground="#242424"
        ).place(anchor='c', relx=0.5, rely=0.46)

        email_var = StringVar()
        ttk.Entry(
            self.frame,
            textvariable=email_var,
            foreground='#4e4e4e',
            font='monospace 10'
        ).place(anchor='c', width=250, height=35, relx=0.5, rely=0.52)

        ttk.Label(
            self.frame,
            text='Password',
            font='sans-serif 11',
            foreground="#242424"
        ).place(anchor='c', relx=0.5, rely=0.63)

        password_var = StringVar()
        ttk.Entry(
            self.frame,
            textvariable=password_var,
            foreground='#4e4e4e',
            font='monospace 10',
            show='*',
        ).place(anchor='c', width=250, height=35, relx=0.5, rely=0.69)

        Button(
            self.frame,
            text='LOGIN',
            background='#0052ea',
            activebackground='#0052ea',
            foreground='white',
            activeforeground='white',
            font='monospace 13 bold',
            command=self.authenticate
        ).place(anchor='c', width=250, height=45, relx=0.5, rely=0.8)
    
    def authenticate(self):
        dashboad_page = DashboardPage(self.window)
        dashboad_page.initialize()