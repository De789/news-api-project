from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import NewsArticle
from pydantic import BaseModel
from typing import List
from datetime import datetime

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Pydantic schema for response
class NewsArticleOut(BaseModel):
    id: int
    title: str
    description: str | None
    url: str
    published_at: datetime
    fetched_at: datetime

    class Config:
        orm_mode = True


# Endpoint to get news by date
@app.get('/news', response_model=List[NewsArticleOut])
def get_news(date: str = Query(...), db: Session = Depends(get_db)):
    try:
        dt = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise HTTPException(status_code=400, detail='Invalid date format')

    start = datetime.combine(dt, datetime.min.time())
    end = datetime.combine(dt, datetime.max.time())

    articles = db.query(NewsArticle).filter(
        NewsArticle.published_at >= start,
        NewsArticle.published_at <= end
    ).all()

    return articles
