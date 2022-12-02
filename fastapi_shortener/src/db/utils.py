from ..config import config
from . import models

def get_db():
    db = config.session_local()
    try:
        yield db
    finally:
        db.close()
        
models.Base.metadata.create_all(bind=config.engine)