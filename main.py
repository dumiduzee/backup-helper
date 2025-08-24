from fastapi import FastAPI
from .api.user.routes import router as user_router

app = FastAPI()

#include user based routes
app.include_router(prefix="/api/v1/user",router=user_router)

