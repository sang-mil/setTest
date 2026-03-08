from fastapi import FastAPI
from sqlalchemy import create_engine
from fastapi.middleware.cors import CORSMiddleware
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

engine = create_engine(DATABASE_URL)

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/db")
def test_db():
    with engine.connect() as conn:
        result = conn.execute("SELECT 1")
    return {"db": "connected"}