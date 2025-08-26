from fastapi import APIRouter,Depends,Request
from ...limiter import limiter  # <-- updated import
from .exceptions import ConfigCreationException, ValueErrorr
from .services import create_config_service, login_service
from ..db import get_db
from .schemas import ConfigCreateSchema, LoginInputSchema, response
from typing import Annotated
from supabase import Client

#router for user based routes
auth_router = APIRouter(tags=["login"])
admin_router = APIRouter(tags=["admin"])


#login endpoint to both user and admin
@auth_router.post("/login")
@limiter.limit("5/minute")
def user_login(request:Request,login_key:LoginInputSchema,db:Annotated[Client,Depends(get_db)]):
    #pass the key into service layer
    result = login_service(login_key.model_dump(),db)
    #return the details
    if result is None:
        raise ValueErrorr(detail="Something went wrong while validating key")
    return result

#=====================admin routes===========================================

#add config to the system
@admin_router.post("/")
@limiter.limit("30/minute")
def create_config(request:Request,config:ConfigCreateSchema,db:Annotated[Client,Depends(get_db)]):
    #pass config data to service layer
    result = create_config_service(config=config.model_dump(),db=db)
    if result:
        return response(message="Config creation succuss!!")
    raise ConfigCreationException()