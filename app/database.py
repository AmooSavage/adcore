from pymongo import MongoClient


class MongoDB:
    def __init__(self):
        self.client = None
        self.database = None

    def connect(self, mongo_uri: str, db_name: str):
        if not self.client:
            self.client = MongoClient(mongo_uri)
            self.database = self.client[db_name]
        return self.database

    def get_collection(self, collection_name: str):
        if not self.database:
            raise RuntimeError("Database not connected. Call 'connect' first.")
        return self.database[collection_name]


# Singleton for database
mongo_instance = MongoDB()


# Lazy-loading utility
def get_database():
    return mongo_instance
