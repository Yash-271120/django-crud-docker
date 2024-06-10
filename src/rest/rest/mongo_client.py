from pymongo import MongoClient
import os

class MongoDBClient:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name):
        return self.db[collection_name]
    
mongo_client = MongoDBClient('mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"], 'test_db')