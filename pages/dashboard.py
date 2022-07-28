from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cairosvg import svg2png
from PIL import ImageTk, Image

from common import Database
from models import Product
from models import User
from models import Sale

from io import BytesIO
import os

from pages import LabelPage

class DashboardPage(LabelPage):
    '''
    Dashboard Page
    '''

    def populate(self):
        '''
        Instance Method for retrieving count of 
        products and users

        @params None
        @return NOne
        '''

        self.sales_count['text'] = Sale.count()
        self.products_count['text'] = Product.count()
        self.users_count['text'] = User.count()

    def content(self):
        ''''
        Create dashboard page components
        '''

        products_card = ttk.LabelFrame(
            self,
            width=350,
            height=150
        )

        sales_card = ttk.LabelFrame(
            self,
            width=350,
            height=150
        )

        users_card = ttk.LabelFrame(
            self,
            width=350,
            height=150
        )

        ttk.Label(
            sales_card,
            text='Sales',
            image=self.assets['sales'],
            compound='top',
            font='Helvetica 15',
            foreground='#4f4f4f',
            borderwidth=2
        ).pack(side='left', padx=5)

        self.sales_count = ttk.Label(
            sales_card,
            text='0',
            foreground='#0052ea',
            font='monospace 60'
        )
        self.sales_count.pack(side='right', padx=5)

        ttk.Label(
            products_card,
            text='Products',
            image=self.assets['products'],
            compound='top',
            font='Helvetica 15',
            foreground='#4f4f4f',
            borderwidth=2
        ).pack(side='left', padx=5)

        self.products_count = ttk.Label(
            products_card,
            text='0',
            foreground='#0052ea',
            font='monospace 60'
        )
        self.products_count.pack(side='right', padx=5)

        ttk.Label(
            users_card,
            text='Users',
            image=self.assets['users'],
            compound='top',
            font='Helvetica 15',
            foreground='#4f4f4f',
            borderwidth=2
        ).pack(side='left', padx=5)

        self.users_count = ttk.Label(
            users_card,
            text='0',
            foreground='#0052ea',
            font='monospace 60',
        )
        
        self.users_count.pack(side='right', padx=5)

        sales_card.place(anchor='c', relx=0.4, rely=0.4)
        products_card.place(anchor='c', relx=0.6, rely=0.4)
        users_card.place(anchor='c', relx=0.4, rely=0.65)

        self.after(5, self.populate)
