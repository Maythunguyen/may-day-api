from pydantic import BaseModel

class JournalEntry(BaseModel):
    userId: str
    title: str
    content: str
    tag: str
    mood: str