from localdb.liblocaldb import json_handler, nosql_handler
import os


def set_verbose_logging(boolean):
    json_handler.VERBOSE_LOGGING = boolean


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
        self.col_path = f'.localdb_storage/{self.parent_db.name}/{self.name}'
        if not os.path.exists(self.col_path):
            os.mkdir(self.col_path)

    def insertOne(self, target_dict):
        target_dict, id = nosql_handler.generateID(target_dict)
        save(target_dict, self.parent_db.name, self.name, id)
        return id

    def insertMany(self, target_dict_list):
        id_list = []
        for target_dict in target_dict_list:
            target_dict, id = nosql_handler.generateID(target_dict)
            save(target_dict, self.parent_db.name, self.name, id)
            id_list.append(id)
        return id_list

    def findByID(self, id):
        return load(self.parent_db.name, self.name, id)

    def findOne(self, search_dict, boolean_relation="and"):
        """
        Returns first matching document.
        Default boolean relation is "and" for multiple search keys.
        """
        search_items = []
        target_json = None
        for key in search_dict.keys():
            search_items.append([key, search_dict[key], 0])

        for filename in os.listdir(self.col_path):
            if filename.endswith('.json'):
                id = filename.replace('.json', '')
                input_json = load(self.parent_db.name, self.name, id)
                parsed_dict = json_handler.parseJSON(input_json)
                for key in parsed_dict.keys():
                    for i in range(len(search_items)):
                        search_key, search_value, _ = search_items[i]
                        if key == search_key:
                            if parsed_dict[key] == search_value:
                                search_items[i][2] = 1
                            else:
                                search_items[i][2] = -1

                results = [row[2] for row in search_items]
                
                if boolean_relation == "and":
                    if (-1 in results) or (0 in results):
                        continue
                    else:
                        target_json = input_json
                        break

                if boolean_relation == "or":
                    if 1 in results:
                        target_json = input_json
                        break

        return target_json

    def findMany(self, search_dict, boolean_relation="and"):
        """
        Returns all matching document(s).
        Default boolean relation is "and" for multiple search keys.
        """
        search_items = []
        target_json_list = []
        for key in search_dict.keys():
            search_items.append([key, search_dict[key], 0])

        for filename in os.listdir(self.col_path):
            if filename.endswith('.json'):
                id = filename.replace('.json', '')
                input_json = load(self.parent_db.name, self.name, id)
                parsed_dict = json_handler.parseJSON(input_json)
                for key in parsed_dict.keys():
                    for i in range(len(search_items)):
                        search_key, search_value, _ = search_items[i]
                        if key == search_key:
                            if parsed_dict[key] == search_value:
                                search_items[i][2] = 1
                            else:
                                search_items[i][2] = -1

                results = [row[2] for row in search_items]

                if boolean_relation == "and":
                    if (-1 in results) or (0 in results):
                        continue
                    else:
                        target_json_list.append(input_json)
                        break

                if boolean_relation == "or":
                    if 1 in results:
                        target_json_list.append(input_json)
                        break

        return target_json_list

    def find(self, search_dict, boolean_relation="and"):
        """
        Same as findMany().
        Returns all matching document(s).
        Default boolean relation is "and" for multiple search keys.
        """
        return self.findMany(search_dict, boolean_relation)
