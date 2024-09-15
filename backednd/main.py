from fastapi import FastAPI, Depends
from schemas import CreateUser
from db import SessionLocal
from schemas import CreateUser, UserInDB
from crud import *

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_user", response_model=UserInDB)
def create_user(user:CreateUser, db = Depends(get_db)):
    pass 

