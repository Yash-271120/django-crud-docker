from django.http import JsonResponse,HttpRequest
from django.views import View
from bson import ObjectId
from ..mongo_client import mongo_client
from .todo_service import TodoService


todo_service = TodoService(mongo_client)

class TodoListView(View):
    def get(self, request:HttpRequest):
        todos = todo_service.find_all_todos()
        return JsonResponse({
            'todos': todos
        })
    
    def post(self, request):
        todo = request.POST.dict()
        inserted_todo = TodoService(mongo_client).create(todo)
        return JsonResponse({"_id": str(inserted_todo._id)}, status=201)