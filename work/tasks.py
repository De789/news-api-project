from celery import Celery
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os
from database import SessionLocal
from models import NewsArticle
from sqlalchemy.orm import Session
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Celery
celery = Celery(
    'tasks',
    broker=os.getenv('REDIS_BROKER'),
    backend=os.getenv('CELERY_BACKEND')
)

# NewsAPI key
NEWSAPI_KEY = os.getenv('NEWSAPI_KEY')


@celery.task
def fetch_news():
    client = NewsApiClient(api_key=NEWSAPI_KEY)
    
    try:
        res = client.get_top_headlines(language='en', page_size=10)
    except Exception as e:
        print(f"Error fetching news: {e}")
        return

    db: Session = SessionLocal()
    try:
        for a in res.get('articles', []):
            if not a.get('publishedAt') or not a.get('title') or not a.get('url'):
                continue

            article = NewsArticle(
                title=a.get('title'),
                description=a.get('description'),
                url=a.get('url'),
                published_at=datetime.fromisoformat(a.get('publishedAt').replace('Z', '+00:00'))
            )
            db.add(article)
        db.commit()
    except Exception as e:
        db.rollback()
        print(f"Error saving to DB: {e}")
    finally:
        db.close()
