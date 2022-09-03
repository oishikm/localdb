from localdb.liblocaldb import json_handler, nosql_handler
import os

def save(input_obj, db_name='default', collection_name='default', id='default'):
    if type(input_obj) is not str:
        target_json = json_handler.createJSON(input_obj)
    else:
        target_json = input_obj
    json_handler.saveJSON(target_json, db_name, collection_name, id)

def load(db_name, collection_name, id):
    return json_handler.loadJSON(db_name, collection_name, id)

class Database():
    def __init__(self, db_name):
        self.name = db_name
        if not os.path.exists('.localdb_storage'):
            os.mkdir('.localdb_storage')
            os.mkdir(f'.localdb_storage/{self.name}')

        if not os.path.exists(f'.localdb_storage/{self.name}'):
            os.mkdir(f'.localdb_storage/{self.name}')

class Collection():
    def __init__(self, col_name, db):
        self.name = col_name
        self.parent_db = db
        if not os.path.exists(f'.localdb_storage/{self.parent_db.name}/{self.name}'):
            os.mkdir(f'.localdb_storage/{self.parent_db.name}/{self.name}')

    def insertOne(self, target_dict):
        target_dict, id = nosql_handler.generateID(target_dict)
        save(target_dict, self.parent_db.name, self.name, id)
        return id

    def findByID(self, id):
        return load(self.parent_db.name, self.name, id)
