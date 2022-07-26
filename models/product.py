from common import Database
from models import Model


class Product(Model):
    '''A model class for product'''
    TABLE_NAME = 'Products'

    def __init__(self, name, price, quantity, image, created_at=None, updated_at=None, id=None):
        super().__init__()
        self.name = name
        self.price = price
        self.quantity = quantity
        self.image = image

    def add(self):
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
    
    
    def json(self)-> dict:
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
