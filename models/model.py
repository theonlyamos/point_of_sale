from datetime import datetime
from typing import Dict, List
import uuid


from common import Database
from common import Utils
#from models import Project
#from models import Function


class Model():
    '''A model class'''
    TABLE_NAME = ''

    def __init__(self, created_at=None, updated_at=None, id=None):
        self.created_at = (datetime.utcnow()).strftime("%a %b %d %Y %H:%M:%S") \
            if not created_at else created_at
        self.updated_at = (datetime.utcnow()).strftime("%a %b %d %Y %H:%M:%S") \
            if not updated_at else updated_at
        self.id = uuid.uuid4() if not id else str(id)

    def save(self):
        '''
        Instance Method for saving Model instance to database

        @params None
        @return None
        '''

        data = {}

        return Database.insert(Model.TABLE_NAME, data)
    
    @classmethod
    def update(cls, id, update: Dict):
        '''
        Class Method for updating model in database

        @param update Content to be update in dictionary format
        @return None
        '''

        return Database.update(cls.TABLE_NAME, id, update)
    
    @classmethod
    def delete(cls, id):
        '''
        Class Method for updating model in database

        @param update Content to be update in dictionary format
        @return None
        '''

        return Database.delete(cls.TABLE_NAME, id)
    
    @classmethod
    def count(cls)-> int:
        '''
        Class Method for counting Model Projects

        @params None
        @return int Count of Projects
        '''

        return Database.count(cls.TABLE_NAME)

    @classmethod
    def get(cls, _id = None):
        '''
        Class Method for retrieving function(s) by _id 
        or all if _id is None

        @param _id ID of the function in database
        @return Function instance(s)
        '''

        if _id is None:
            return [cls(**elem) for elem in Database.find(cls.TABLE_NAME)]

        model = Database.find_one(cls.TABLE_NAME, {'id': _id})
        return cls(**model) if model else None
    
    @classmethod
    def find(cls, params: dict)-> list:
        '''
        Class Method for retrieving models
        by provided parameters

        @param params
        @return List[Model]
        '''

        return [cls(**elem) for elem in Database.find(cls.TABLE_NAME, params)]
    
    @classmethod
    def search(cls, columnname: str, search: str):
        '''
        Class Method for retrieving products
        by their names

        @param name
        @return Product Instance
        '''

        sql = f"SELECT * from {cls.TABLE_NAME} WHERE "
        sql += f"{columnname} LIKE '%{search}%'"
        
        return [cls(**elem) for elem in Database.query(sql)]
    
    def json(self)-> Dict:
        '''
        Instance Method for converting Model Instance to Dict

        @paramas None
        @return dict() format of Function instance
        '''

        return {}
