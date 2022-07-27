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

from io import BytesIO
import os

class MainLayoutPage():
    '''
    Main Layout Page
    '''

    def __init__(self, window):
        self.window = window
    
    def build_assets(self):
        self.assets = {'dashboard'  : {'name': 'chart-line.svg'},
                       'products'   : {'name': 'shopping-basket.svg'},
                       'users'      : {'name': 'users.svg'},
                       'settings'   : {'name': 'chart-pie.svg'},
                       'addButton'  : {'name': 'plus.svg'}}
        
        for key in self.assets.keys():
            img_path = self.assets[key]['name']
            img_io = BytesIO()
            img_url = os.path.realpath(os.path.join(os.curdir, 'assets', img_path))
            svg2png(url=img_url, write_to=img_io)
            self.assets[key]['image'] = ImageTk.PhotoImage(Image.open(img_io).resize((50, 50)))
    
    def initialize(self):
        '''
        Create Dashboard Page Component
        '''

        self.build_assets()
        self.create_frames()
        self.sidebar()

        self.current_frame = self.dashboard
        self.sidebar_frame.pack(side='left', fill='none', anchor='n')
        self.dashboard.pack(side='right', expand=1, fill='both')

    def create_frames(self):
        '''
        Create Main Page Frames
        [Sidebar, Dashboard, Products,
         Users, Settings]
        '''

        self.window.geometry("900x400")
        self.window.title('Dashboard - Supermarket Billing System')

        self.sidebar_frame = ttk.Frame(
            self.window,
            width=200,
            height=400
        )

        self.dashboard = DashboardPage(
            self.window,
            text='Dashboard',
            width=700,
            height=400
        )

        self.products = ProductsPage(
            self.window,
            text='Products',
            width=700,
            height=400
        )

        self.users_frame = ttk.LabelFrame(
            self.window,
            text='Users',
            width=700,
            height=400
        )

        self.settings_frame = ttk.LabelFrame(
            self.window,
            text='Settings',
            width=700,
            height=400
        )

    def sidebar(self):
        '''
        Create Sidebar Components
        [Menu]
        '''
        
        Button(
            self.sidebar_frame,
            text='Dashboard',
            image=self.assets['dashboard']['image'],
            compound='top',
            activebackground='#da1039',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.dashboard)
        ).pack(fill='x', side='top')

        Button(
            self.sidebar_frame,
            text='Products',
            image=self.assets['products']['image'],
            compound='top',
            activebackground='#da1039',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.products)
        ).pack(fill='x')

        Button(
            self.sidebar_frame,
            text='Users',
            image=self.assets['users']['image'],
            compound='top',
            activebackground='#da1039',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.users_frame)
        ).pack(fill='x')

        Button(
            self.sidebar_frame,
            text='Settings',
            image=self.assets['settings']['image'],
            compound='top',
            activebackground='#da1039',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.settings_frame)
        ).pack(fill='x')

    def change_page(self, next_frame):
        self.current_frame.pack_forget()
        self.current_frame = next_frame
        self.current_frame.pack(side='right', expand=1, fill='both')
