from localdb import localdb

sample_json = {
    "name" : "GenericName",
    "age" : 99
}

localdb.save(sample_json, 'TestDB', 'GenericPerson')
print(localdb.load('TestDB', 'GenericPerson'))
