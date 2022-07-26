from common import Database
from models import Model
from models import SaleItem

class Sales(Model):
    '''A model class for Sales'''
    TABLE_NAME = 'Sales'

    def __init__(self, total):
        super().__init__(self, created_at=None, updated_at=None, id=None)
        self.total = total

    def add(self):
        '''
        Instance Method for saving Sales instance to database

        @params None
        @return None
        '''

        data = {
            "total": self.total
        }

        return Database.insert(Sales.TABLE_NAME, data)
    
    def items(self)-> list[SaleItem]:
        '''
        Instance Method for retrieving purchased Items

        @params None
        @return List[Saleitem]
        '''

        saleitems = SaleItem.get_by_sales(self.id)
        print(saleitems)
        return saleitems
    
    def json(self)-> dict:
        '''
        Instance Method for converting Sales Instance to Dict

        @paramas None
        @return dict() format of Product instance
        '''

        return {
            "id": str(self.id),
            "total": self.total,
            "items": self.items(),
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
