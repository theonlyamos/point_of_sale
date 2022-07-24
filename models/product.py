from datetime import datetime
from typing import Dict, List
import uuid


from common import Database
from common import Utils
from models import Model
#from models import Function


class Product(Model):
    '''A model class for product'''
    TABLE_NAME = 'In_Stocks'

    def __init__(self, name, price, quantity, image):
        super().__init__(self, created_at=None, updated_at=None, id=None)
        self.name = name
        self.price = price
        self.quantity = quantity
        self.image = image

    def save(self):
        '''
        Instance Method for saving Product instance to database

        @params None
        @return None
        '''

        data = {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "image": self.image
        }

        return Database.insert(Product.TABLE_NAME, data)
    
    
    def json(self)-> Dict:
        '''
        Instance Method for converting Product Instance to Dict

        @paramas None
        @return dict() format of Function instance
        '''

        return {
            "id": str(self.id),
            "name": self.name,
            "quantity": self.quantity,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
