from fastapi import APIRouter
from .schemas import LoginInputSchema

#router for user based routes
router = APIRouter(tags=["user"])

#login endpoint to both user and admin
@router.post("/login")
def user_login(login_key:LoginInputSchema):
    #pass the key into service layer
    #get username and user type
    #return the details
    pass