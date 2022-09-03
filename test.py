from localdb import localdb

sample_json = {
    "name" : "GenericName",
    "age" : 99
}

db = localdb.Database('TestDB')
collection = localdb.Collection('GenericPerson', db)
id = collection.insertOne(sample_json)

print(collection.findByID(id))
