#!python3
# -*- coding: utf-8 -*-
# @Date    : 2022-07-22 11:42:39
# @Author  : Amos Amissah (theonlyamos@gmai.com)
# @Link    : link
# @Version : 1.0.0

import os
from mysql import connector
from constants import HOST, PASSWORD, USER


class Database:
    db = None
    cursor = None

    @staticmethod
    def initialize():
        db = connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database="Billing_System",
            auth_plugin='mysql_native_password'
        )

        cursor = db.cursor(buffered=True, dictionary=True)
        Database.db = db
        Database.cursor = cursor
    
    @staticmethod
    def insert(table: str, data: dict):

        query = f'INSERT INTO {table}('
        query += ', '.join(data.keys())
        query += ") VALUES('"

        values = [str(val) for val in data.values()]
        query += "','".join(values)
        query += "')"
        try:
            Database.cursor.execute(query, None)
            Database.db.commit()

            if data:
                return Database.cursor.rowcount

            resp = [x for x in Database.cursor.fetchall()]
            return {'status': 'success', 'result': resp}

        except Exception as e:
            return {'status': 'Error', 'message': str(e)}
    
    @staticmethod
    def update(table: str, id: int, data: dict):

        query = f'UPDATE {table} SET'
        for key, value in data:
            query += f" {key}='{value},'"
        
        query = query.rstrip(',')
        
        query += f" WHERE id={id}"
        
        print(query)

        try:
            Database.cursor.execute(query, None)
            Database.db.commit()

            if data:
                return Database.cursor.rowcount

            resp = [x for x in Database.cursor.fetchall()]
            return {'status': 'success', 'result': resp}

        except Exception as e:
            return {'status': 'Error', 'message': str(e)}
    
    @staticmethod
    def find(table: str, params: dict = {}):
        query = f'SELECT * FROM {table}'

        if len(params.keys()):
            query += ' WHERE '
            for key, value in params:
                query += f"{key}='{value}'"
        
        try:
            Database.cursor.execute(query, None)
            Database.db.commit()

            return [x for x in Database.cursor.fetchall()]

        except Exception as e:
            return {'status': 'Error', 'message': str(e)}
    
    @staticmethod
    def find_one(table: str, params: dict = {}):
        query = f'SELECT * FROM {table}'

        if len(params.keys()):
            query += ' WHERE '
            for key, value in params:
                query += f"{key}='{value}'"
        
        try:
            Database.cursor.execute(query, None)
            Database.db.commit()

            resp = [x for x in Database.cursor.fetchall()]
            return resp[0]

        except Exception as e:
            return {'status': 'Error', 'message': str(e)}
    
    @staticmethod
    def count(table: str, params: dict = {}):
        query = f'SELECT * FROM {table}'

        if len(params.keys()):
            query += ' WHERE '
            for key, value in params:
                query += f"{key}='{value}'"

        try:
            Database.cursor.execute(query, None)
            Database.db.commit()

            return Database.cursor.rowcount

        except Exception as e:
            return {'status': 'Error', 'message': str(e)}