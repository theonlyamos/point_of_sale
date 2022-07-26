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

    def add(self):
        '''
        Instance Method for saving Model instance to database

        @params None
        @return None
        '''

        data = {}

        return Database.insert(Model.TABLE_NAME, data)
    
    def update(self, update: Dict):
        '''
        Instance Method for updating model in database

        @param update Content to be update in dictionary format
        @return None
        '''

        Database.update(Model.TABLE_NAME, self.id, update)
    
    @classmethod
    def count(cls)-> int:
        '''
        Class Method for counting Model Projects

        @params None
        @return int Count of Projects
        '''

        return Database.count(cls.TABLE_NAME)
    
    def json(self)-> Dict:
        '''
        Instance Method for converting Model Instance to Dict

        @paramas None
        @return dict() format of Function instance
        '''

        return {}

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
