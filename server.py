from fastapi import FastAPI,HTTPException,Request
from fastapi.responses import JSONResponse
from .api.user.routes import auth_router 
from .api.user.routes import admin_router
from .api.settings import settings
#rate limiter imports 
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from .limiter import limiter
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI()

# Add SlowAPI middleware
app.add_middleware(SlowAPIMiddleware)

#rate limiter handler
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

#include user based routes
app.include_router(prefix="/api/v1/auth",router=auth_router)
app.include_router(prefix="/api/v1/admin",router=admin_router)

@app.exception_handler(HTTPException)
async def exception_handler(request:Request,exc:HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail" : exc.detail}
    )

