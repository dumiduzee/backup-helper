from fastapi import Depends,APIRouter,status,Request
from ...limiter import limiter  # <-- updated import
from .exceptions import ConfigCreationException, DeleteConfigException, ValueErrorr
from .services import (create_config_service, delete_config_service, get_configs_service,
    login_service)
from ..db import get_db
from .schemas import ConfigCreateSchema, LoginInputSchema, response
from typing import Annotated
from supabase import Client

#router for user based routes
auth_router = APIRouter(tags=["login"])
admin_router = APIRouter(tags=["admin"])
user_router = APIRouter(tags=["user"])


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

#=====================user routes===========================================

#get all available configs
@user_router.get("/")
@limiter.limit("30/minute")
def get_configs(request:Request,db:Annotated[Client,Depends(get_db)]):
    pass
    #pass request to service layer
    result = get_configs_service(db=db)
    if result:
        return response(message="Configs fetch done",data=result.data)
    return response(message="No any available configs")

#=====================admin routes===========================================

#add config to the system
@admin_router.post("/")
@limiter.limit("30/minute")
def create_config(request:Request,config:ConfigCreateSchema,db:Annotated[Client,Depends(get_db)]):
    #pass config data to service layer
    result = create_config_service(config=config.model_dump(),db=db)
    if result:
        return response(message="Config creation succuss!!",data=None)
    raise ConfigCreationException()

#get all available configs
@admin_router.get("/")
@limiter.limit("30/minute")
def get_configs(request:Request,db:Annotated[Client,Depends(get_db)]):
    pass
    #pass request to service layer
    result = get_configs_service(db=db)
    if result:
        return response(message="Configs fetch done",data=result.data)
    return response(message="No any available configs")

#delete specific config from the system
@admin_router.delete("/:id")
@limiter.limit("30/minute")
def delete_configs(request:Request,id:str,db:Annotated[Client,Depends(get_db)]):
    result = delete_config_service(id,db)
    if result:
        return response(message="Config deleted!",data=None)
    raise DeleteConfigException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Something went wrong while deleting the config!")


#add new user to the system
@admin_router.post("/add-client")
@limiter.limit("30/minute")
def add_client(request:Request,db:Annotated[Client,Depends(get_db)]):
    pass