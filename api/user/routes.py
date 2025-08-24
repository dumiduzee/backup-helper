from fastapi import APIRouter

#router for user based routes
router = APIRouter(tags=["user"])

@router.get("/")
def root():
    return "hi"