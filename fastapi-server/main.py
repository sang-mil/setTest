from fastapi import FastAPI
from sqlalchemy import create_engine, text
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(
    DATABASE_URL,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True
)

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/db")
def db_test():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return {"db": "connected"}

@app.get("/data")
def data():
    return JSONResponse(
        {"data": "example"},
        headers={"Cache-Control": "public, max-age=60"}
    )