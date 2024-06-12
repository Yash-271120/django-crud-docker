class MongoDBConnectionError(Exception):
    """Exception raised for errors in the MongoDB connection."""
    def __init__(self, message="Failed to connect to MongoDB"):
        self.message = message
        super().__init__(self.message)

class TodoNotFoundError(Exception):
    """Exception raised when a user is not found in the database."""
    def __init__(self, user_id, message="User not found for ID:"):
        self.user_id = user_id
        self.message = f"{message} {user_id}"
        super().__init__(self.message)
        
class InvalidTodoIdError(Exception):
    """Exception raised for invalid user ID format."""
    def __init__(self, message="Invalid user ID"):
        self.message = message 
        super().__init__(self.message)
        
class TodoOperationError(Exception):
    """Exception raised for general user operation errors."""
    def __init__(self, operation, message="An error occurred during the operation"):
        self.operation = operation
        self.message = f"{message}: {operation}"
        super().__init__(self.message)