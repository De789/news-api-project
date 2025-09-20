from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Model for creating a news article
class NewsArticleCreate(BaseModel):
    source: Optional[str]
    author: Optional[str]
    title: str
    description: Optional[str]
    url: str
    published_at: datetime


# Model for outputting a news article
class NewsArticleOut(BaseModel):
    title: str
    description: Optional[str]
    url: str
    published_at: datetime

    class Config:
        orm_mode = True
