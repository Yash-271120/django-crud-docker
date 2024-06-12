from django.core.exceptions import ValidationError

def validate_todo_data(todo_data):
    if not todo_data.get('content'):
        raise ValidationError("Content is required")
    if not isinstance(todo_data.get('content'), str):
        raise ValidationError("Content must be a string")
    
def validate_todo_id(todo_id):
    if not todo_id or len(todo_id) != 24:
        raise ValidationError("Invalid todo id")
        