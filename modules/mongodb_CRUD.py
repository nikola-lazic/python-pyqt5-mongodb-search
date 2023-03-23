# Here you write CRUD (create, read, update and delete) functions
# Examples:
# def read_mongodb()
# def create_connection()...

from pymongo import MongoClient


def create_connection():
    """Connect to MongoDB and return object referrence"""

    client = MongoClient("mongodb://localhost:27017/")  # Default local host and port
    try:
        info = client.server_info()  # Forces a call.
        print("Connection is established")
    except ServerSelectionTimeoutError:
        # https://stackoverflow.com/questions/45240106/pymongo-exception-handling-not-working-right-in-python-3
        return None

    db = client["Test-database"]  # Getting a Database
    print(f"Database name: {db.name}")  # Print database name
    return db


def find_matches(query_parameters):
    """Find records that match the query term"""

    db = create_connection()

    # Return None if error occured during connection
    if db == None:
        return None

    all_results = []

    # This will search in all collections
    for collection_name in db.list_collection_names():
        for results in db[collection_name].find(query_parameters):
            all_results.append(results)

    print(f"Query parameters: {query_parameters}")
    return all_results
