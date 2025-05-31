from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import atmosphere

app = FastAPI()

# CORS middleware to allow frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount API routes
app.include_router(atmosphere.router, prefix="/api")
