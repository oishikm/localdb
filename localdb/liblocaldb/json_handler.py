import json
import os


def createJSON(input_dict):
    output_json = json.dumps(input_dict, indent=4)
    
    print(f'[INFO] Success : Created JSON')
    return output_json


def parseJSON(input_json):
    output_dict = json.loads(input_json)

    print('[INFO] Success : Parsed JSON')
    return output_dict


def saveJSON(input_json, db_name='default', col_name='default', name='default'):
    if not os.path.exists('.localdb_storage'):
        os.mkdir('.localdb_storage')
        os.mkdir(f'.localdb_storage/{db_name}')

    if not os.path.exists(f'.localdb_storage/{db_name}'):
        os.mkdir(f'.localdb_storage/{db_name}')

    if not os.path.exists(f'.localdb_storage/{db_name}/{col_name}'):
        os.mkdir(f'.localdb_storage/{db_name}/{col_name}')

    filename = f'.localdb_storage/{db_name}/{col_name}/{name}.json'
    with open(filename, "w") as jsonfile:
        jsonfile.write(input_json)

    print(f'[INFO] Success : Saved JSON at \'{filename}\'')


def loadJSON(db_name, col_name, name):
    filename = f'.localdb_storage/{db_name}/{col_name}/{name}.json'
    output_str = None
    
    if os.path.exists(filename):
        with open(filename, "r") as jsonfile:
            output_str = str(jsonfile.read())
    
    print(f'[INFO] Success : Loaded JSON from \'{filename}\'')
    return output_str
