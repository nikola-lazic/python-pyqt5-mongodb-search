# This script will create an Test-database with 2 collections.
# Data from JSON files will be imported into each collection.

import pymongo
import json

# establish connection to MongoDB
client = pymongo.MongoClient()

# create a database called "Test-database"
db = client["Test-database"]

# import first JSON file into collection "www.somesite1.com"
with open("data/www.somesite1.com.json", "r") as f:
    data = json.load(f)
    collection = db["www.somesite1.com"]
    collection.insert_many(data)


# import second JSON file into collection "www.somesite2.com"
with open("data/www.somesite2.com.json", "r") as f:
    data = json.load(f)
    collection = db["www.somesite2.com"]
    collection.insert_many(data)
