from fastapi import APIRouter,Depends,Request
from ...limiter import limiter  # <-- updated import
from .exceptions import ValueErrorr
from .services import login_service
from ..db import get_db
from .schemas import LoginInputSchema
from typing import Annotated
from supabase import Client

#router for user based routes
router = APIRouter(tags=["user"])

#login endpoint to both user and admin
@router.post("/login")
@limiter.limit("5/minute")
def user_login(request:Request,login_key:LoginInputSchema,db:Annotated[Client,Depends(get_db)]):
    #pass the key into service layer
    result = login_service(login_key.model_dump(),db)
    #return the details
    if result is None:
        raise ValueErrorr(detail="Something went wrong while validating key")
    return result