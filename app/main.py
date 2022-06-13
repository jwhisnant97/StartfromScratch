# StartfromScratch/main.py

import validators
from fastapi import FastAPI, HTTPException

# from fastapi.responses import RedirectResponse
# from starlette.datastructures import URL

from . import schemas
from .database import SessionLocal# , engine
# from .config import get_settings

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

@app.get("/")
def hello():
    return {"message": "Hello World!"}

@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")
    return f"TODO: Create database entry for: {url.target_url}"

@app.get("/{url_key}")
def foo():
    return "bar"

@app.get("/admin/{secret_key}")
def foo():
    return "bar"

@app.delete("/admin/{secret_key}")
def foo():
    return "bar"