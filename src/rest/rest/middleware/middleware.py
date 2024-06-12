import json
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import ValidationError
from ..responses import ErrorResponse
from ..todo.todo_validator import validate_todo_data,validate_todo_id

class ValidateRequestMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method  in ["POST","PUT"]:
            try:
                if request.content_type == 'application/json':
                    request_data = json.loads(request.body)
                else:
                    request_data = request.POST.dict()
                    
                if view_func.__name__ == 'TodoListView':
                    validate_todo_data(request_data)
                elif view_func.__name__ == 'TodoDetailView' and request.method == 'PUT':
                    validate_todo_data(request_data)
                    validate_todo_id(view_kwargs.get('todo_id'))
            except ValidationError as e:
                return ErrorResponse(str(e), status=400)
            except json.JSONDecodeError:
                return ErrorResponse("Invalid JSON data", status=400)
            
        elif request.method == 'GET' or request.method == 'DELETE':
            if view_func.__name__ == 'TodoDetailView':
                try:
                    validate_todo_id(view_kwargs.get('todo_id'))
                except ValidationError as e:
                    return ErrorResponse(str(e), status=400)
        return None
                    