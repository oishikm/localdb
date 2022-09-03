from localdb import localdb

sample_json = {
    "name" : "GenericName",
    "age" : 99
}

db = localdb.Database('TestDB')
collection = localdb.Collection('GenericPerson', db)
id = collection.insert(sample_json)

print(collection.find_by_id(id))
