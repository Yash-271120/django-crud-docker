from django.http import HttpRequest, HttpResponse
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId
from ..mongo_client import MongoDBClient
from ..exceptions import InvalidTodoIdError,TodoNotFoundError,TodoOperationError

class TodoService:
    def __init__(self,client:MongoDBClient):
        self.collection = client.get_collection('todos')
    
    def find_all_todos(self):
        try:
            return list(self.collection.find())
        except PyMongoError as e:
            raise TodoOperationError(f"An error occurred while retrieving todos: {e}")

    def find_by_id(self, id):
        try:
            if not ObjectId.is_valid(id):
                raise InvalidTodoIdError("Invalid Todo ID")
            todo = self.collection.find_one({"_id": ObjectId(id)})
            if not todo:
                raise TodoNotFoundError(f"Todo not found for ID: {id}")
            return todo
        except PyMongoError as e:
            raise TodoOperationError(f"An error occurred while retrieving todo: {e}")
    
    def create(self, todo):
        try:
            result = self.collection.insert_one(todo)
            return result.inserted_id
        except PyMongoError as e:
            raise TodoOperationError(f"An error occurred while creating todo: {e}")
    
    def update(self, id, todo):
        try:
            if not ObjectId.is_valid(id):
                raise InvalidTodoIdError("Invalid Todo ID")
            result = self.collection.update_one({"_id": ObjectId(id)}, {"$set": todo})
            if result.modified_count == 0:
                raise TodoNotFoundError(f"Todo not found for ID: {id}")        
        except PyMongoError as e:
            raise TodoOperationError(f"An error occurred while updating todo: {e}")
    
    def delete(self, id):
        print("here")
        try:
            if not ObjectId.is_valid(id):
                raise InvalidTodoIdError("Invalid Todo ID")
            result = self.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count == 0:
                raise TodoNotFoundError(f"Todo not found for ID: {id}")
        except PyMongoError as e:
            raise TodoOperationError(f"An error occurred while deleting todo: {e}")
    