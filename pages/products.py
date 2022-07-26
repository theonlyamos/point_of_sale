from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cairosvg import svg2png
from PIL import ImageTk, Image

from pages import LabelPage
from models import Product

from io import BytesIO
import os

from pages.newproduct import AddProductPage

class ProductsPage(LabelPage):
    '''
    Products List Page
    '''

    def update_products_table(self, product):
        self.products_table.insert(parent='', index='end', iid=self.last_product_id, text='',
                                    values=product)
    
    def populate_products_table(self):
        self.products_list = Product.get()
        self.last_product_id = 0
        
        if type(self.products_list) is list:
            self.products_count['text'] = len(self.products_list)
            
            for product in self.products_list:
                self.last_product_id =  self.products_list.index(product)
                
                prod = (self.last_product_id+1, product.name, product.price, product.quantity)
                self.update_products_table(prod)
                
        else:
            print(self.products_list)
    
    def add_product_window(self):
        AddProductPage(
            self.master
        )
    
    def content(self):
        ''''
        Create products page components
        '''

        img_path = 'plus-square.svg'
        img_io = BytesIO()
        img_url = os.path.realpath(os.path.join(os.curdir, 'assets', img_path))
        svg2png(url=img_url, write_to=img_io)
        #plus_img = ImageTk.PhotoImage(Image.open(img_io).resize((50, 50)))

        tools_frame = ttk.Frame(
            self
        )

        products_card = ttk.Frame(
            tools_frame
        )

        ttk.Label(
            products_card,
            text='Products',
            image=self.assets['products']['image'],
            compound='top',
            font='Helvetica 15',
            foreground='#4f4f4f',
            borderwidth=2
        ).pack(side='left', padx=10)

        self.products_count = ttk.Label(
            products_card,
            text='0',
            foreground='gray',
            font='monospace 50',
        )
        self.products_count.pack(side='right', padx=10)

        products_card.pack(side='left', padx=30)

        Button(
            tools_frame,
            text='Add Product',
            command=self.add_product_window
        ).pack(side='right', padx=20, pady=5)

        tools_frame.pack(anchor='e')

        self.products_table = ttk.Treeview(self)
        self.products_table['columns'] = ('item_id', 'item_name', 'item_price',
                                     'item_quantity')
        self.products_table.column('#0', width=0, stretch=NO)
        self.products_table.column('item_id', anchor=CENTER)
        self.products_table.column('item_name', anchor=CENTER)
        self.products_table.column('item_price', anchor=CENTER)
        self.products_table.column('item_quantity', anchor=CENTER)
        self.products_table.heading('#0', text='', anchor=CENTER)
        self.products_table.heading('item_id', text='ID', anchor=CENTER)
        self.products_table.heading('item_name', text='Name', anchor=CENTER)
        self.products_table.heading('item_price', text='Price', anchor=CENTER)
        self.products_table.heading('item_quantity', text='In Stock', anchor=CENTER)
        self.products_table.pack(fill='x', expand=1)

        self.after(5, self.populate_products_table)

    