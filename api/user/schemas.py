from pydantic import BaseModel,field_validator

class LoginInputSchema(BaseModel):
    login_key : str 
    @field_validator("login_key")
    @classmethod
    def validate_login_key(cls,v):
        if len(v) == 0:
            pass
        if len(v) < 8:
            pass
        return v
