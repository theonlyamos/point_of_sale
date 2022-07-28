from curses.ascii import isdigit
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cairosvg import svg2png
from PIL import ImageTk, Image

from common import Database
from models import Product
from pages.products import ProductsPage
from pages.dashboard import DashboardPage
from pages.sales import SalesPage

from io import BytesIO
import os

from assets import ChartAreaIcon, ShoppingCartIcon, ShoppingBasketIcon,\
                    UsersIcon, ChartPieIcon, PlusIcon

class MainLayoutPage():
    '''
    Main Layout Page
    '''

    def __init__(self, window):
        self.window = window
    
    def build_assets(self):
        self.assets = {
            'dashboard'  : ImageTk.PhotoImage(ChartAreaIcon.resize((50, 50))),
            'sales'      : ImageTk.PhotoImage(ShoppingCartIcon.resize((50, 50))),
            'products'   : ImageTk.PhotoImage(ShoppingBasketIcon.resize((50, 50))),
            'users'      : ImageTk.PhotoImage(UsersIcon.resize((50, 50))),
            'settings'   : ImageTk.PhotoImage(ChartPieIcon.resize((50, 50))),
            'addButton'  : ImageTk.PhotoImage(PlusIcon.resize((50, 50)))}
    
    def initialize(self):
        '''
        Create Dashboard Page Component
        '''

        self.build_assets()
        self.create_frames()
        self.sidebar()

        self.current_frame = self.dashboard
        self.sidebar_frame.pack(side='left', fill='none', anchor='n')
        self.current_frame.pack(side='right', expand=1, fill='both')

    def create_frames(self):
        '''
        Create Main Page Frames
        [Sidebar, Dashboard, Products,
         Users, Settings]
        '''

        self.window.geometry("950x500")
        self.window.title('Dashboard - Supermarket Billing System')

        self.sidebar_frame = ttk.Frame(
            self.window,
            width=200
        )

        self.sales = SalesPage(
            self.window,
            text='Sales'
        )

        self.dashboard = DashboardPage(
            self.window,
            text='Dashboard'
        )

        self.products = ProductsPage(
            self.window,
            text='Products'
        )

        self.users_frame = ttk.LabelFrame(
            self.window,
            text='Users'
        )

        self.settings_frame = ttk.LabelFrame(
            self.window,
            text='Settings'
        )

    def sidebar(self):
        '''
        Create Sidebar Components
        [Menu]
        '''
        
        Button(
            self.sidebar_frame,
            text='Dashboard',
            image=self.assets['dashboard'],
            compound='top',
            activebackground='#da1039',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.dashboard)
        ).pack(fill='x', side='top')

        Button(
            self.sidebar_frame,
            text='Sales',
            image=self.assets['sales'],
            compound='top',
            activebackground='#da1039',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.sales)
        ).pack(fill='x')

        Button(
            self.sidebar_frame,
            text='Products',
            image=self.assets['products'],
            compound='top',
            activebackground='#da1039',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.products)
        ).pack(fill='x')

        Button(
            self.sidebar_frame,
            text='Users',
            image=self.assets['users'],
            compound='top',
            activebackground='#da1039',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.users_frame)
        ).pack(fill='x')

        Button(
            self.sidebar_frame,
            text='Settings',
            image=self.assets['settings'],
            compound='top',
            activebackground='#da1039',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.settings_frame)
        ).pack(fill='x')

    def change_page(self, next_frame):
        self.current_frame.pack_forget()
        self.current_frame = next_frame
        self.current_frame.pack(side='right', expand=1, fill='both')
