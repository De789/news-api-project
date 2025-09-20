from sqlalchemy.orm import Session
from models import NewsArticle
from schemas import NewsArticleCreate
from datetime import datetime


def create_article(db: Session, article: NewsArticleCreate):
    db_article = NewsArticle(
    source=article.source,
    author=article.author,
    title=article.title,
    description=article.description,
    url=article.url,
    published_at=article.published_at,

)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_articles_by_date(db: Session, date):
    # date is a datetime.date
  start = datetime.combine(date, datetime.min.time())
  end = datetime.combine(date, datetime.max.time())
  return db.query(NewsArticle).filter(NewsArticle.published_at >= start, NewsArticle.published_at <= end).all()