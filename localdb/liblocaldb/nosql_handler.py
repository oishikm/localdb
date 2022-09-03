import time

def generateID(target_dict):
    if "_id" not in target_dict.keys():
        id = 'T'+str(time.time()).replace('.','F')
        target_dict["_id"] = id

    return target_dict, id
