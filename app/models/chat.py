from pydantic import BaseModel

class MessageRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str