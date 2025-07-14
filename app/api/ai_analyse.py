from fastapi import APIRouter
from app.services.ai_service import AIService
from app.models.journal import JournalEntry

api_router = APIRouter()

@api_router.post("/ai_analyse")
async def analyse_journal(entry: JournalEntry):
    ai_service = AIService()
    entry_text = f"{entry.title}\n\n{entry.content}\n\nTag: {entry.tag}\nMood: {entry.mood}"
    result = ai_service.analyse_single_entry(entry_text)
    return {"result": result}
