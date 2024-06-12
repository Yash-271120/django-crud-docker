from django.http import JsonResponse

class SuccessResponse(JsonResponse):
    def __init__(self, data=None, message="Success", status=200, **kwargs):
        response_data = {
            "status": "success",
            "message": message,
            "data": data
        }
        super().__init__(response_data, status=status, **kwargs)

class ErrorResponse(JsonResponse):
    def __init__(self, error_message, status=400, **kwargs):
        response_data = {
            "status": "error",
            "message": error_message
        }
        super().__init__(response_data, status=status, **kwargs)