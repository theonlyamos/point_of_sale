from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cairosvg import svg2png
from PIL import ImageTk, Image

from io import BytesIO
import os

from pages import LabelPage
from models import Product
from assets import AddImageIcon

from pages.newproduct import AddProductPage
from pages.updateproduct import UpdateProductPage

class ProductsPage(LabelPage):
    '''
    Products List Page
    '''

    def update_products_table(self, product):
        self.products_table.insert(parent='', index=0, iid=self.last_product_id, text='',
                                    values=product)
    
    def populate_products_table(self):
        self.products_list = Product.get()
        self.last_product_id = 0
        
        if type(self.products_list) is list:
            self.products_count['text'] = len(self.products_list)
            
            for product in self.products_list:
                self.last_product_id =  self.products_list.index(product)
                
                prod = (product.id, product.name, product.price, product.quantity)
                self.update_products_table(prod)
                
        else:
            print(self.products_list)
    
    def add_product_window(self):
        product_window = AddProductPage(
            self.master
        )
        product = product_window.show()
        if product:
            self.last_product_id = int(product[0])
            self.products_count['text'] = str(int(product[0]))
            self.update_products_table(product)
    
    def update_product(self):
        if len(self.products_table.selection()):
            selected = self.products_table.item(self.products_table.selection()[0])
            
            product = Product.get(selected['values'][0])

            product_window = UpdateProductPage(
                product,
                self.master
            )
            
            result = product_window.show()
            
            if result:
                self.products_table.item(self.products_table.selection()[0], text='', values=result)
        else:
            messagebox.showwarning('Error Message', 'Select a row to update')
    
    def delete_product(self):
        if len(self.products_table.selection()):
            selected = self.products_table.item(self.products_table.selection()[0])
            
            confirm = messagebox.askyesno(
                title='Deletion Confirmation',
                message='Delete this product?'
            )
            if confirm:
                result = Product.delete(selected['values'][0])
                
                if result:
                    self.products_table.delete(self.products_table.selection()[0])
                    count = int(self.products_count['text'])
                    self.products_count['text'] = str(count-1)
        else:
            messagebox.showwarning('Error Message', 'Select a row to delete')
    
    def search_products(self, event):
        for item in self.products_table.get_children():
                self.products_table.delete(item)
        try:
            if len(self.product_search_var.get()) > 1:
                products = Product.search('name', self.product_search_var.get())
                for product in products:
                    self.update_products_table((product.id, product.name,
                    product.price, product.quantity))
            else:
                self.populate_products_table()
        except:
            pass
    
    def content(self):
        ''''
        Create products page components
        '''
        plus_img = ImageTk.PhotoImage(AddImageIcon.resize((50, 50)))

        tools_frame = ttk.Frame(
            self
        )

        products_card = ttk.Frame(
            tools_frame
        )

        ttk.Label(
            products_card,
            text='Products',
            image=self.assets['products'],
            compound='top',
            font='Helvetica 15',
            foreground='#4f4f4f',
            borderwidth=2
        ).grid(column=0, row=0)

        self.products_count = ttk.Label(
            products_card,
            text='0',
            foreground='gray',
            font='monospace 50',
        )
        self.products_count.grid(column=1, row=0, padx=10)

        products_card.grid(column=0, row=0, sticky='nw')

        self.product_search_var = StringVar()
        self.product_search_var.set('Product Search')
        self.product_search_entry = ttk.Entry(
            tools_frame,
            textvariable=self.product_search_var,
            foreground='#4e4e4e',
            font='monospace 10',
            justify='center',
            width=25
        )
        self.product_search_entry.bind('<FocusIn>', lambda ev: self.product_search_var.set(''))
        self.product_search_entry.bind('<KeyRelease>', self.search_products)
        self.product_search_entry.grid(column=1, row=1, padx=15, ipady=5)

        Button(
            tools_frame,
            text='Add Product',
            command=self.add_product_window
        ).grid(column=2, row=1, padx=15)

        Button(
            tools_frame,
            text='Update Product',
            command=self.update_product
        ).grid(column=3, row=1, padx=15)

        Button(
            tools_frame,
            text='Delete Product',
            command=self.delete_product
        ).grid(column=4, row=1, padx=15)

        tools_frame.grid(column=0, columnspan=5, row=1, padx=10, pady=5, sticky='nw')

        self.products_table = ttk.Treeview(self, height=14)
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

        #self.products_table.bind("<<TreeviewSelect>>", self.update_product)
        self.products_table.grid(column=0, row=2, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.products_table.yview)
        self.products_table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(column=1, row=2, sticky='ns')

        self.after(5, self.populate_products_table)

    