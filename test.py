from localdb import localdb

# Uncomment below line to get verbose logging in console
# localdb.set_verbose_logging(True)

sample_json = {
    "name": "Yoda",
    "age": 877
}

db = localdb.Database('StarWars')
collection = localdb.Collection('RevengeOfTheSith', db)

# Insert single document into collection using insertOne() and serach by ID
id = collection.insertOne(sample_json)
print(collection.findByID(id))

# Insert multiple documents into collection using insertMany()
collection.insertMany([
    {
        "name": "General Kenobi",
        "age": 38
    },
    {
        "name": "General Grievous",
        "age": 40
    }
])

print(collection.findOne({"name": "General Kenobi"}))
print(collection.findOne({"age": 877, "name": "Yoda"}, "or"))
print(collection.findOne({"age": 877, "name": "Yoda"})) # default is "and"

found_list = collection.findMany({"age": 38, "name": "General Kenobi"}) # default is "and"
for found_json in found_list:
    print(found_json)

# find() is same as findMany()
found_list = collection.find({"age": 40, "name": "General Grievous"}) # default is "and"
for found_json in found_list:
    print(found_json)
