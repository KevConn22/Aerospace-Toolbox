from fastapi import FastAPI
from routers import atmosphere

app = FastAPI()
app.include_router(atmosphere.router, prefix="/api")

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your Vercel domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
