from fastapi import APIRouter
from app.services.ai_service import AIService
from app.models.journal import JournalEntry
from app.models.bulk import BulkRequest

api_router = APIRouter()

@api_router.post("/ai_analyse")
async def analyse_journal(entry: JournalEntry):
    ai_service = AIService()
    entry_text = f"{entry.title}\n\n{entry.content}\n\nTag: {entry.tag}\nMood: {entry.mood}"
    result = ai_service.analyse_single_entry(entry_text)
    return {"result": result}



@api_router.post("/ai_analyse_bulk")
async def analyse_journal_bulk(data: BulkRequest):
    """
    data might be: { "entries": [ { "title": "...", "content": "...", ... }, ... ] }
    We'll combine these into one big prompt for aggregated analysis.
    """
    ai_service = AIService()

    # Build a combined string from all entries
    combined_text = ""
    for idx, e in enumerate(data["entries"]):
        combined_text += (
            f"Entry #{idx+1}:\n"
            f"Title: {e.title}\n"      
            f"Content: {e.content}\n" 
            f"Tag: {e.tag}\n"
            f"Mood: {e.mood}\n\n"
        )

    # Pass combined_text to AI
    bulk_result = ai_service.analyse_bulk_entries(combined_text)
    return {"bulk_result": bulk_result}