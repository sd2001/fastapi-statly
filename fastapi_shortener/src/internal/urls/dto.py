from pydantic import BaseModel
from typing import Union

class shorten_url(BaseModel):
    target_url: str
    key: str
    clicks: int
    topics: str
    is_active: bool
        
class expect_url(BaseModel):
    target_url: str
    topics: Union[str, None] = None