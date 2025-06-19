import os
import json

HANDLERS_DIR = "handlers"
ROUTES_FILE = "routes.json"

route = input("Route name (ex: /users): ").strip()
if not route.startswith("/"):
    route = "/" + route

module = route.strip("/").replace("/", "_")
function = f"get_{module}"

methods = input("HTTP Methods (ex: GET,POST,PUT): ").upper().replace(" ", "").split(",")

handler_path = os.path.join(HANDLERS_DIR, f"{module}.py")

# Create handler file
if not os.path.exists(handler_path):
    with open(handler_path, "w") as f:
        f.write(f"""from fastapi import Request

async def {function}(request: Request):
    return {{"message": "Route message: '{route}'"}}
""")
    print(f"Handler created: {handler_path}")
else:
    print(f"Handler already exists: {handler_path}")

# Update routes.json
with open(ROUTES_FILE, "r") as f:
    rotas = json.load(f)

rotas[route] = {
    "handler": f"handlers.{module}:{function}",
    "methods": methods
}

with open(ROUTES_FILE, "w") as f:
    json.dump(rotas, f, indent=2)

print(f"Route added to {ROUTES_FILE}")
