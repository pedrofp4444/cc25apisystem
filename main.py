from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import importlib
import json
from config import AUTH_ON
from auth import token_auth_middleware

app = FastAPI()

# Applies the authentication middleware, if necessary
if AUTH_ON:
    app.middleware("http")(token_auth_middleware)

# Reads and loads the routes from the JSON file
with open("routes.json", "r") as f:
    routes_config = json.load(f)

for route_path, routes_info in routes_config.items():
    module_path, func_name = routes_info["handler"].split(":")
    methods = routes_info.get("methods", ["GET"])

    try:
        module = importlib.import_module(module_path)
        handler_func = getattr(module, func_name)
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading the route {route_path}: {e}")
        continue

    async def endpoint(request: Request, handler_func=handler_func):
        return await handler_func(request)

    app.add_api_route(route_path, endpoint, methods=methods)

@app.get("/")
def root():
    return {"msg": "API System working"}
