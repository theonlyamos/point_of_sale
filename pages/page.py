from tkinter import ttk
from cairosvg import svg2png
from PIL import ImageTk, Image

from io import BytesIO
import os

class Page(ttk.Frame):
    '''
    Initial Class for Pages Frame.
    Inherits from ttk.Frame
    '''

    def __init__(self, master=None, **kw):
        super().__init__()
        self.build_assets
        self.content()

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

    def content(self):
        pass

class LabelPage(ttk.LabelFrame):
    '''
    Initial Class for Pages Frame.
    Inherits from ttk.Frame
    '''

    def __init__(self, master=None, **kw):
        super().__init__()
        self.build_assets()
        self.content()

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
    
    def content(self):
        pass