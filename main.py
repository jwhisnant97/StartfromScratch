# StartfromScratch/main.py

from fastapi import FastAPI, Depends, HTTPException, Request

# from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
# from starlette.datastructures import URL

# from . import crud, schemas, models
from .database import SessionLocal #, engine
# from .config import get_settings

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def hello():
    return {"message": "Hello World!"}
