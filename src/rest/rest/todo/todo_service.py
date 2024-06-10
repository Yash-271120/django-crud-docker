from django.http import HttpRequest, HttpResponse
from ..mongo_client import MongoDBClient

class TodoService:
    def __init__(self,client:MongoDBClient):
        self.collection = client.get_collection('todos')
    
    def find_all_todos(self):
        return list(self.collection.find({}))

    def find_by_id(self, id):
        return self.collection.find_one({"_id": id})
    
    def create(self, todo):
        return self.collection.insert_one(todo)
    
    def update(self, id, todo):
        return self.collection.update_one({"_id": id}, {"$set": todo})
    
    def delete(self, id):
        return self.collection.delete_one({"_id": id})
    