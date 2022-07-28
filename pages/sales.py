from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk

from models import Sale
from pages import LabelPage
from pages.newsale import AddSalePage
from pages.updatesale import UpdateSalePage
from assets import AddImageIcon

class SalesPage(LabelPage):
    '''
    Sales List Page
    '''

    def update_sales_table(self, sale):
        self.sales_table.insert(parent='', index=0, iid=sale[0], text='',
                                    values=sale)
    
    def populate_sales_table(self):
        self.sales_list = Sale.get()

        if type(self.sales_list) is list:
            self.sales_count['text'] = len(self.sales_list)
            
            for sale in self.sales_list:
                sale = sale.json()
                
                self.update_sales_table((sale['id'], sale['count'], 
                                         sale['total'], sale['updated_at']))
                
        else:
            print(self.sales_list)
    
    def add_sale_window(self):
        sale_window = AddSalePage(
            self.master
        )
        sale = sale_window.show()
        if sale:
            self.sales_count['text'] = str(int(sale[0]))
            self.update_sales_table(sale)
    
    def update_sale_window(self, event=None):
        if len(self.sales_table.selection()):
            selected = self.sales_table.item(self.sales_table.selection()[0])
            
            sale = Sale.get(selected['values'][0])

            sale_window = UpdateSalePage(
                sale,
                self.master
            )
            
            result = sale_window.show()
            
            if result:
                self.sales_table.item(self.sales_table.selection()[0], text='', values=result)
        else:
            messagebox.showwarning('Error Message', 'Select a row to update')
    
    # def delete_sale(self):
    #     if len(self.sales_table.selection()):
    #         selected = self.sales_table.item(self.sales_table.selection()[0])
            
    #         confirm = messagebox.askyesno(
    #             title='Deletion Confirmation',
    #             message='Delete this sale?'
    #         )
    #         if confirm:
    #             result = Sale.delete(selected['values'][0])
                
    #             if result:
    #                 self.sales_table.delete(self.sales_table.selection()[0])
    #                 count = int(self.sales_count['text'])
    #                 self.sales_count['text'] = str(count-1)
    #     else:
    #         messagebox.showwarning('Error Message', 'Select a row to delete')
    
    def content(self):
        ''''
        Create sales page components
        '''
        plus_img = ImageTk.PhotoImage(AddImageIcon.resize((50, 50)))

        tools_frame = ttk.Frame(
            self
        )

        sales_card = ttk.Frame(
            tools_frame
        )

        ttk.Label(
            sales_card,
            text='Sales',
            image=self.assets['sales'],
            compound='top',
            font='Helvetica 15',
            foreground='#4f4f4f',
            borderwidth=2
        ).grid(column=0, row=0)

        self.sales_count = ttk.Label(
            sales_card,
            text='0',
            foreground='gray',
            font='monospace 50',
        )
        self.sales_count.grid(column=1, row=0, padx=10)

        sales_card.grid(column=0, row=0, sticky='nw')

        self.filter_var = StringVar()
        self.filter_var.set('Today')
        ttk.Combobox(
            tools_frame,
            textvariable=self.filter_var,
            font='monospace 10',
            foreground='#4e4e4e',
            background='white',
            values=('Today', 'Yesterday', 'This Week', 'This Month', 'Custom'),
            state='readonly',
            justify='center'
        ).grid(column=1, row=1, padx=15, ipady=5)

        Button(
            tools_frame,
            text='Add Sale',
            command=self.add_sale_window
        ).grid(column=2, row=1, padx=15)

        Button(
            tools_frame,
            text='Update Sale',
            command=self.update_sale_window
        ).grid(column=3, row=1, padx=15)

        Button(
            tools_frame,
            text='Delete Sale',
            #command=self.delete_sale
        ).grid(column=4, row=1, padx=15)

        tools_frame.grid(column=0, columnspan=5, row=1, padx=10, pady=5, sticky='nw')

        self.sales_table = ttk.Treeview(self, height=14)
        self.sales_table['columns'] = ('item_id', 'count', 'total',
                                     'date')
        self.sales_table.column('#0', width=0, stretch=NO)
        self.sales_table.column('item_id', anchor=CENTER)
        self.sales_table.column('count', anchor=CENTER)
        self.sales_table.column('total', anchor=CENTER)
        self.sales_table.column('date', anchor=CENTER)

        self.sales_table.heading('#0', text='', anchor=CENTER)
        self.sales_table.heading('item_id', text='ID', anchor=CENTER)
        self.sales_table.heading('count', text='Items Count', anchor=CENTER)
        self.sales_table.heading('total', text='Total', anchor=CENTER)
        self.sales_table.heading('date', text='Date', anchor=CENTER)

        self.sales_table.bind("<<TreeviewSelect>>", self.update_sale_window)
        self.sales_table.grid(column=0, row=2, sticky='nsew')

        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.sales_table.yview)
        self.sales_table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(column=1, row=2, sticky='ns')

        self.after(5, self.populate_sales_table)

    