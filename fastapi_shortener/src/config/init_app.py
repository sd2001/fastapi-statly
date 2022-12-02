from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from ..handlers.url import router
from . import config

app = FastAPI()


@app.get("/check")
def read_root():
    return "URL shortener server up and running..."


app.include_router(router)