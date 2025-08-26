from pydantic import BaseModel,field_validator,Field
from .exceptions import ValueErrorr


#succuss response
class response(BaseModel):
    succuss:bool = Field(default=True)
    message:str

#Schema for the login data
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

#schema for admin's config creation process
class ConfigCreateSchema(BaseModel):
    config_name : str = Field(...,examples=["Airtel"])
    config : str = Field(...,examples=["vless:://....."])