from sqlalchemy import Column, Integer, String, Date, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class NewsArticle(Base):
     __tablename__ = 'news_articles'
id = Column(Integer, primary_key=True, index=True)
source = Column(String(255), nullable=True)
author = Column(String(255), nullable=True)
title = Column(String(1024), nullable=False)
description = Column(Text, nullable=True)
url = Column(String(2048), nullable=False)
published_at = Column(DateTime, nullable=False)
fetched_at = Column(DateTime(timezone=True), server_default=func.now())