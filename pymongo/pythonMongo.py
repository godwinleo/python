import pymongo


myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

print(myclient.list_database_names())


dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")


print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

mycol = mydb["customers"]


#----------------------insert---------------------------------------

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)


#----------------------Return the _id Field
The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.

Example
Insert another record in the "customers" collection, and return the value of the _id field:

mydict = { "name": "Peter", "address": "Lowstreet 27" }

x = mycol.insert_one(mydict)

print(x.inserted_id)