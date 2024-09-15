from fastapi import FastAPI
from schemas import CreateUser
from db import SessionLocal

app = FastAPI()

@app.post("create_user")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

