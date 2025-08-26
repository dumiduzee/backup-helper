from fastapi import  HTTPException,status

class ValueErrorr(HTTPException):
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = None):
        super().__init__(status_code, detail)

class UnauthorizedKey(HTTPException):
    def __init__(self, status_code=status.HTTP_401_UNAUTHORIZED, detail = None):
        super().__init__(status_code, detail)

#config creation exceptions
class ConfigCreationException(HTTPException):
    def __init__(self, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "Something went wrong"):
        super().__init__(status_code, detail)

#delete config exceptions
class DeleteConfigException(HTTPException):
    def __init__(self, status_code=None, detail = None):
        super().__init__(status_code, detail)


#add client exceptions
class AddClientexception(HTTPException):
    def __init__(self, status_code=None, detail = None):
        super().__init__(status_code, detail)


#delete client exceptions
class DeleteClientException(HTTPException):
    def __init__(self, status_code=None, detail = None):
        super().__init__(status_code, detail)