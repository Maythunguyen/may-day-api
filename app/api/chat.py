from fastapi import APIRouter
from app.services.ai_service import AIService
from app.models.chat import MessageRequest, ChatResponse

chat_router = APIRouter()
ai_service = AIService()

@chat_router.post("/message_with_ai")
async def message_with_ai_endpoint(message: MessageRequest):
    print(f"📩 Received message: {message}")
    ai_reply = ai_service.message_with_ai(message.message)
    return ChatResponse(reply=ai_reply)