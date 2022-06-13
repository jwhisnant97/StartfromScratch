# StartfromScratch/main.py

from fastapi import FastAPI, Depends, HTTPException, Request

# from fastapi.responses import RedirectResponse
# from sqlalchemy.orm import Session
# from starlette.datastructures import URL

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World!"}
