from fastapi import FastAPI
from .routers import archive

app = FastAPI()
routers = [archive]

for r in routers:
    app.include_router(r.router)