from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")  # Default local host and port

db = client["Test-database"]  # Getting a Database
print(f"Database name is: {db.name}")  # Print database name

find_all_collections = db.list_collection_names()  # List all collections in mongodb
print(f"List of all collections: {find_all_collections}")
print(f"Type: {type(find_all_collections)}")  # This is a list

query = "Test-3"  # Defined by user


# This will search query in 1 collection ("www.somesite1.com")
for item in db.www.somesite1.com.find({"meta-title": query}):
    print(item)
    print(type(item))  # This is dictionary


# This will search in all collections
for collection_name in db.list_collection_names():
    # print("collection:{}".format(collection_name))
    for all_results in db[collection_name].find({"meta-title": query}):
        print(all_results)


# This will limit the number of results
limit = 1
counter = 0
for collection_name in db.list_collection_names():
    # print("collection:{}".format(collection_name))
    counter = counter + 1
    if counter <= limit:
        for all_results in db[collection_name].find({"meta-title": query}):
            print(all_results)
    else:
        pass


# This is searching with multiple criteria. Useful for filtering:
imported = "Yes"
for collection_name in db.list_collection_names():
    # print("collection:{}".format(collection_name))
    for all_results in db[collection_name].find(
        {"meta-title": query, "imported": imported}
    ):
        print(all_results)
