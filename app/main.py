# StartfromScratch/main.py
import secrets

import validators
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

# from fastapi.responses import RedirectResponse
# from starlette.datastructures import URL

from . import schemas, models
from .database import SessionLocal , engine
# from .config import get_settings

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

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

@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your provided URL is not valid")

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url

@app.get("/{url_key}")
def foo():
    return "bar"

@app.get("/admin/{secret_key}")
def foo():
    return "bar"

@app.delete("/admin/{secret_key}")
def foo():
    return "bar"