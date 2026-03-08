from fastapi import FastAPI
from sqlalchemy import create_engine
import os

app = FastAPI()

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