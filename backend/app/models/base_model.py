from pymongo import MongoClient, ASCENDING

mongo_client = None
mongo_db = None


def init_db(app):
    global mongo_client, mongo_db
    uri = app.config.get("MONGO_URI")
    if not uri:
        raise ValueError("MONGO_URI is required")
    mongo_client = MongoClient(uri)
    mongo_db = mongo_client[app.config["MONGO_DB_NAME"]]
    create_indexes()


def get_collection(name):
    return mongo_db[name]


def create_indexes():
    get_collection("users").create_index([("email", ASCENDING)], unique=True)
    get_collection("careers").create_index([("career_title", ASCENDING)])
