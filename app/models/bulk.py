from pydantic import BaseModel
from typing import List
from app.models.journal import JournalEntry

class BulkRequest(BaseModel):
    entries: List[JournalEntry]

    class Config:
        extra = "allow"