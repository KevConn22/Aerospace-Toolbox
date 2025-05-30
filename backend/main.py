from fastapi import FastAPI
from routers import atmosphere

app = FastAPI()
app.include_router(atmosphere.router, prefix="/api")
