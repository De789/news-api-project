from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NewsArticleCreate(BaseModel):
source: Optional[str]
author: Optional[str]
title: str
description: Optional[str]
url: str
published_at: datetime


class NewsArticleOut(BaseModel):
id: int
source: Optional[str]
author: Optional[str]
title: str
description: Optional[str]
url: str
published_at: datetime
fetched_at: datetime


class Config:
# orm_mode = Tr