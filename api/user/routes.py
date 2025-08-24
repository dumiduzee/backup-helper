from fastapi import APIRouter
from .schemas import LoginInputSchema

#router for user based routes
router = APIRouter(tags=["user"])

@router.post("/login")
def user_login(login_key:LoginInputSchema):
    return "hi"