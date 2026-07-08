from datetime import datetime


class DefaultGenericResponseDto:
    def __init__(self, success: bool, message: str, data: None):
        self.success = success
        self.message = message
        self.timestamp = datetime.now()
        self.data = data
        
    def to_dict(self):
        return {
            "success": self.success,
            "message": self.message,
            "timestamp": self.timestamp.isoformat(),
            "data": self.data,
        }
