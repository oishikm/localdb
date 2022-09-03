from localdb import localdb

# Uncomment below line to get verbose logging in console
# localdb.set_verbose_logging(True)

sample_json = {
    "name": "GenericName",
    "age": 99
}

db = localdb.Database('TestDB')
collection = localdb.Collection('GenericPerson', db)

# Uncomment below 2 line to insert 1 document from sample_json into collection and serach by ID
# id = collection.insertOne(sample_json)
# print(collection.findByID(id))

print(collection.findOne({"age": 99, "name": "GenericName"}, "or"))
print(collection.findOne({"age": 99, "name": "GenericName"})) # default is "and"

found_list = collection.findMany({"age": 99, "name": "GenericName"}) # default is "and"
for found_json in found_list:
    print(found_json)

# find() is same as findMany()
found_list = collection.find({"age": 99, "name": "GenericName"}) # default is "and"
for found_json in found_list:
    print(found_json)
