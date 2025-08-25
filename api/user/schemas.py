from pydantic import BaseModel,field_validator
from .exceptions import ValueErrorr

class LoginInputSchema(BaseModel):
    login_key : str 
    @field_validator("login_key")
    @classmethod
    def validate_login_key(cls,v):
        if len(v) == 0:
            raise ValueErrorr(detail="Login key cannot be empty")
        if len(v) < 8:
            raise ValueErrorr(detail="Seems to be a invalid login key")
        return v
