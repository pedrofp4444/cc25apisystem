from fastapi import Request
from fastapi.responses import JSONResponse
from config import VALID_TOKENS

async def token_auth_middleware(request: Request, call_next):
    token = request.query_params.get("token")
    if token not in VALID_TOKENS:
        return JSONResponse(status_code=401, content={"error": "Invalid token"})
    response = await call_next(request)
    return response
