# app/main.py

from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Include payment routes
app.include_router(router, prefix="/api", tags=["Payments"])


@app.get("/")
async def root():
    return {"message": "Welcome to the Payment Management API"}
