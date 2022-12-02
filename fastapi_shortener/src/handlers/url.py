from ..db.utils import get_db
from ..internal.urls.dto import shorten_url, expect_url
from ..internal.urls.utils import shorten_url_utils, forward_to_target_url, stats_url

from fastapi import Depends, FastAPI, HTTPException, APIRouter
from sqlalchemy.orm import Session

router = APIRouter(tags=["urls"])

@router.post("/shorten", status_code=201)
def create_url_handler(url: expect_url, db: Session = Depends(get_db)):
    return shorten_url_utils(url, db)

@router.get("/{key}")
def redirect_url_handler(key: str, db: Session = Depends(get_db)):
    return forward_to_target_url(key, db)

@router.get("/stats/{key}")
def stats_url_handler(key: str, db: Session = Depends(get_db)):
    return stats_url(key, db)