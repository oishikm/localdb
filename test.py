from localdb import localdb

sample_json = {
    "name" : "GenericName",
    "age" : 99
}

db = localdb.Database('TestDB')
collection = localdb.Collection('GenericPerson', db)

# Uncomment below line to insert 1 document from sample_json into collection
# id = collection.insertOne(sample_json)

# Uncomment below line to search by ID
# print(collection.findByID(id))

print(collection.findOne( { "age" : 99, "name" : "GenericName2" } )) # default is "and"
print(collection.findOne( { "age" : 99, "name" : "GenericName2" } , "or"))