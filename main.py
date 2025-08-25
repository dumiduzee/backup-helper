from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse
from .api.user.routes import router as user_router

app = FastAPI()

#include user based routes
app.include_router(prefix="/api/v1/user",router=user_router)


@app.exception_handler(HTTPException)
async def exception_handler(request:Request,exc:HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail" : exc.detail}
    )
