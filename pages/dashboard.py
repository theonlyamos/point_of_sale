from curses.ascii import isdigit
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from cairosvg import svg2png
from PIL import ImageTk, Image

from common import Database

from io import BytesIO
import os

class DashboardPage():
    '''
    Dashboad Page
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

        self. build_assets()
        self.create_frames()
        self.create_content()

        self.current_frame = self.dashboard_frame
        self.sidebar_frame.pack(side='left', fill='none', anchor='n')
        self.dashboard_frame.pack(side='right', expand=1, fill='both')
        #self.frame.place(anchor="c", relx=0.5, rely=0.5)

    def update_products_table(self, product):
        self.products_table.insert(parent='', index='end', iid=int(product[0])-1, text='',
                                    values=product)
    
    def populate_products_table(self):
        result = Database.find('In_Stocks')
        self.last_product_id = 0
        
        if type(result) is list:
            self.products_count['text'] = len(result)
            products = [prod.values() for prod in result ]
            
            for product in products:
                product = list(product)
                self.last_product_id =  int(product[0])

                img_link = product[3]
                product[3] = product[4]
                product[4] = img_link
                product = tuple(product)
                self.update_products_table(product)
                
        else:
            print(result)
    
    def add_product(self):
        'Items, Price, Item_image_link, Quantity'
        new_product = {'Items': self.new_product_name_var.get(), 
                'Price': self.new_product_price_var.get(), 
                'Item_image_link': '',
                'Quantity': self.new_product_quantity_var.get()}
        
        result = Database.insert('In_Stocks', new_product)
        
        if result == 1:
            product = (self.last_product_id+1, self.new_product_name_var.get(),
                self.new_product_price_var.get(), self.new_product_quantity_var.get())
            
            self.update_products_table(product)
        else:
            messagebox.showerror('Error Message', result['message'])
        self.new_product_window.destroy()
    
    def show_add_products_window(self):
        self.new_product_window = Toplevel(self.window)
        self.new_product_window.title('Add Product')
        self.new_product_window.geometry("400x500")

        const_url = "add_img.png"
        img_url = os.path.realpath(os.path.join(os.curdir, 'assets', const_url))
        add_img = ImageTk.PhotoImage(Image.open(img_url).resize((60, 50)))

        ttk.Label(
             self.new_product_window,
            text='Add Product',
            font='Helvetica 20 bold',
            foreground='#da1039'
        ).place(anchor='c', relx=0.5, rely=0.15)

        Button(
            self.new_product_window,
            text='Product Image',
            image=add_img,
            compound='left',
            font='Arial 11'
        ).place(anchor='c', width=250, height=80, relx=0.5, rely=0.3)

        ttk.Label(
            self.new_product_window,
            text='Product Name',
            font='sans-serif 11',
            foreground="#242424"
        ).place(anchor='c', relx=0.5, rely=0.42)

        self.new_product_name_var = StringVar()
        ttk.Entry(
            self.new_product_window,
            textvariable=self.new_product_name_var,
            foreground='#4e4e4e',
            font='monospace 10',
            justify='center'
        ).place(anchor='c', width=250, height=35, relx=0.5, rely=0.48)

        ttk.Label(
            self.new_product_window,
            text='Product Price',
            font='sans-serif 11',
            foreground="#242424"
        ).place(anchor='c', relx=0.5, rely=0.56)

        self.new_product_price_var = DoubleVar()
        ttk.Entry(
            self.new_product_window,
            textvariable=self.new_product_price_var,
            foreground='#4e4e4e',
            font='monospace 10',
            justify='center'
        ).place(anchor='c', width=250, height=35, relx=0.5, rely=0.62)

        ttk.Label(
            self.new_product_window,
            text='Product Quantity',
            font='sans-serif 11',
            foreground="#242424"
        ).place(anchor='c', relx=0.5, rely=0.7)

        self.new_product_quantity_var = IntVar()
        ttk.Entry(
            self.new_product_window,
            textvariable=self.new_product_quantity_var,
            foreground='#4e4e4e',
            font='monospace 10',
            justify='center'
        ).place(anchor='c', width=250, height=35, relx=0.5, rely=0.76)

        Button(
            self.new_product_window,
            text='Save',
            background='#0052ea',
            activebackground='#0052ea',
            foreground='white',
            activeforeground='white',
            font='monospace 13 bold',
            command=self.add_product
        ).place(anchor='c', width=250, height=45, relx=0.5, rely=0.86)

        products = Database.find('In_Stocks')
        
        self.new_product_window.mainloop()
    
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

        self.dashboard_frame = ttk.LabelFrame(
            self.window,
            text='Dashboard',
            width=700,
            height=400
        )

        self.products_frame = ttk.LabelFrame(
            self.window,
            text='Products',
            width=700,
            height=400
        )

        self.products_frame.after(5, self.populate_products_table)

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
    
    def create_content(self):
        '''
        Create Dashboard Page Components
        '''

        self.sidebar()
        self.dashboard_content()
        self.products_content()
    
    def dashboard_content(self):
        ''''
        Create main page components
        '''

        products_card = ttk.LabelFrame(
            self.dashboard_frame,
            width=250,
            height=150
        )

        users_card = ttk.LabelFrame(
            self.dashboard_frame,
            width=250,
            height=150
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

        ttk.Label(
            products_card,
            text=self.products_count['text'],
            foreground='#0052ea',
            font='monospace 70',
        ).pack(side='right', padx=10)

        ttk.Label(
            users_card,
            text='Users',
            image=self.assets['users']['image'],
            compound='top',
            font='Helvetica 15',
            foreground='#4f4f4f',
            borderwidth=2
        ).pack(side='left', padx=10)

        ttk.Label(
            users_card,
            text='0',
            foreground='#0052ea',
            font='monospace 70',
        ).pack(side='right', padx=10)

        products_card.place(anchor='c', relx=0.4, rely=0.5)
        users_card.place(anchor='c', relx=0.6, rely=0.5)

    def products_content(self):
        ''''
        Create products page components
        '''

        img_path = 'plus-square.svg'
        img_io = BytesIO()
        img_url = os.path.realpath(os.path.join(os.curdir, 'assets', img_path))
        svg2png(url=img_url, write_to=img_io)
        plus_img = ImageTk.PhotoImage(Image.open(img_io).resize((50, 50)))

        tools_frame = ttk.Frame(
            self.products_frame
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
            command=self.show_add_products_window
        ).pack(side='right', padx=20, pady=5)

        tools_frame.pack(anchor='e')

        self.products_table = ttk.Treeview(self.products_frame)
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
            background='#da1039',
            activebackground='#0052ea',
            state='active',
            foreground='black',
            activeforeground='white',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.dashboard_frame)
        ).pack(fill='x', side='top')

        Button(
            self.sidebar_frame,
            text='Products',
            image=self.assets['products']['image'],
            compound='top',
            background='#da1039',
            activebackground='#0052ea',
            foreground='black',
            activeforeground='white',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.products_frame)
        ).pack(fill='x')

        Button(
            self.sidebar_frame,
            text='Users',
            image=self.assets['users']['image'],
            compound='top',
            background='#da1039',
            activebackground='#0052ea',
            foreground='black',
            activeforeground='white',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.users_frame)
        ).pack(fill='x')

        Button(
            self.sidebar_frame,
            text='Settings',
            image=self.assets['settings']['image'],
            compound='top',
            background='#da1039',
            activebackground='#0052ea',
            foreground='black',
            activeforeground='white',
            font='monospace 13 bold',
            command=lambda: self.change_page(self.settings_frame)
        ).pack(fill='x')

    def change_page(self, next_frame):
        self.current_frame.pack_forget()
        self.current_frame = next_frame
        self.current_frame.pack(side='right', expand=1, fill='both')
