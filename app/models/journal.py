from pydantic import BaseModel
from typing import Optional

class JournalEntry(BaseModel):
    userId: Optional[str] = None
    title: str
    content: str
    tag: str
    mood: str

    class Config:
        extra = "allow"  # <--- let Pydantic ignore extra keys