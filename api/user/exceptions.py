from fastapi import  HTTPException,status

class ValueErrorr(HTTPException):
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = None):
        super().__init__(status_code, detail)