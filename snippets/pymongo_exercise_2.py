# Creating indexes for Full text search
# Reference: # https://www.analyticsvidhya.com/blog/2020/09/mongodb-indexes-pymongo-tutorial/


from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")  # Default local host and port

db = client["Test-database"]  # Getting a Database
print(f"Database name is: {db.name}")  # Print database name

find_all_collections = db.list_collection_names()  # List all collections in mongodb
print(f"List of all collections: {find_all_collections}")
print(f"Type: {type(find_all_collections)}")  # This is a list

query = "Test-3"  # Defined by user

# Drop the index:
# db.www.somesite1.com.drop_index("meta-title_1")

# Create text index in single collection
db.www.somesite1.com.create_index([("meta-title", "text")], name="page-title")


# Create text index in all collections:
for collection_name in db.list_collection_names():
    for all_collections in db[collection_name].create_index(
        [("meta-title", "text")], name="page-title"
    ):
        # print(f"Index: {all_collections}")
        pass

# Print index information
print(db.www.somesite1.com.index_information())

# This will search for text in single collection:
for item in db.www.somesite1.com.find({"$text": {"$search": "example"}}):
    print(f"Results in single collection: {item}")


# This will search for text in all collections
for collection_name in db.list_collection_names():
    for all_results in db[collection_name].find({"$text": {"$search": "example"}}):
        print(f"Results in all collections: {all_results}")
