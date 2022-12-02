import time
import string
from ...db import models
from sqlalchemy.orm import Session

from fastapi.responses import RedirectResponse, JSONResponse


class Codec:
    def __init__(self):
        self.urlMap = {}

    def generate_id(self):
        return int(time.time()) * 1000

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        id = self.generate_id()
        map = string.digits + string.ascii_letters
        s_url = ""
        # Convert Base-62
        while id > 0:
            p = id % 62
            s_url += map[p]
            id = id // 62
        self.urlMap[s_url] = longUrl
        return s_url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.urlMap:
            return self.urlMap[shortUrl]
        return None

codec = Codec()

def shorten_url_utils(url, db: Session):
    shorten_string = codec.encode(url.target_url)
    db_entity = models.URL(
        target_url=url.target_url,
        key=shorten_string,
        is_active=True,
        topics=url.topics,
        clicks=0
    )
    db.add(db_entity)
    db.commit()
    db.refresh(db_entity)
    return db_entity

def update_db_clicks(db: Session, db_url):
    db_url.clicks += 1
    db.commit()
    db.refresh(db_url)

def forward_to_target_url(key: str, db: Session):
    db_url = (
        db.query(models.URL).filter(models.URL.key == key, models.URL.is_active).first()
    )
    if db_url:
        update_db_clicks(db, db_url)
        return RedirectResponse(db_url.target_url)
    else:
        return JSONResponse(status_code=404, content={"message": "Key not found"})
    
def stats_url(key: str, db: Session):
    db_url = (
        db.query(models.URL).filter(models.URL.key == key, models.URL.is_active).first()
    )
    if db_url:
        return db_url
    else:
        return JSONResponse(status_code=404, content={"message": "Key not found"})