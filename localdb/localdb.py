from localdb.liblocaldb import json_handler

def save(input_obj, db_name='default', collection_name='default'):
    if type(input_obj) is not str:
        target_json = json_handler.createJSON(input_obj)
    else:
        target_json = input_obj
    json_handler.saveJSON(target_json, db_name, collection_name)

def load(db_name, collection_name):
    return json_handler.loadJSON(db_name, collection_name)
