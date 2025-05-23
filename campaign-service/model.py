from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Campaign(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    scheduled_time: datetime
    created_by: str
    is_sent: bool = False
