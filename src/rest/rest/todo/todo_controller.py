from django.http import HttpRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
import bson.json_util as json_util
from ..mongo_client import mongo_client
from .todo_service import TodoService
from ..exceptions import TodoNotFoundError,TodoOperationError
from rest.responses import ErrorResponse,SuccessResponse

todo_service = TodoService(mongo_client)
        
class TodoDetailView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    
    def get(self, request, todo_id):
        try:
            todo = todo_service.find_by_id(todo_id)
            return SuccessResponse(json.loads(json_util.dumps(todo)))
        except TodoNotFoundError as e:
            return ErrorResponse(f"Not found: {e}",status=404)
        except TodoOperationError as e:
            return ErrorResponse(f"Server error: {e}",status=500)
        
    def put(self, request, todo_id):
        try:
            todo_data = json.loads(request.body)
            todo_service.update(todo_id, todo_data)
            return SuccessResponse(message="Todo updated successfully")
        except TodoNotFoundError as e:
            return ErrorResponse(f"Not found: {e}",status=404)
        except TodoOperationError as e:
            return ErrorResponse(f"Server error: {e}",status=500)
    
    def delete(self, request, todo_id):
        try:
            todo_service.delete(todo_id)
            return SuccessResponse(message="Todo deleted successfully")
        except TodoNotFoundError as e:
            return ErrorResponse(f"Not found: {e}",status=404)
        except TodoOperationError as e:
            return ErrorResponse(f"Server error: {e}",status=500)
        
        
        
class TodoListView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    
    def get(self, request:HttpRequest):
        try:
            print('Getting all todos')
            todos = todo_service.find_all_todos()
            return SuccessResponse(json.loads(json_util.dumps(todos)))
        except TodoOperationError as e:
            return ErrorResponse(str(e), status=500)
            
    
    def post(self, request):
        try:
            todo_data = json.loads(request.body)
            print(todo_data)
            todo_id = todo_service.create(todo_data)
            return SuccessResponse(data={"id": str(todo_id)}, message="Todo created successfully", status=201)
        except ValueError as e:
            return ErrorResponse(f"Bad request: {e}", status=400)  
        except TodoOperationError as e:
            return ErrorResponse(f"Server error: {e}", status=500)  
    