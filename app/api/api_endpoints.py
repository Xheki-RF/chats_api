import app.crud.crud as crud_operations
from fastapi import Depends, APIRouter
from sqlmodel import Session
from app.db.db import get_session
from app.schemas.schemas import CreateChat, Chat, CreateMessage, Message

chat_router = APIRouter()


# Create chat
@chat_router.post("/chats")
def create_chat(title: str, session: Session = Depends(get_session)) -> Chat:
    return crud_operations.create_chat(title, session)


# Send a message into chat
@chat_router.post("/chats/{id}/messages")
def send_message(id: int, text=CreateMessage, session: Session = Depends(get_session)) -> Message:
    return crud_operations.create_message(id, text, session)


# Get chat and last N messages
@chat_router.get("/chats/{id}")
def get_chat_by_id():
    pass


# Delete chat with all messages
@chat_router.delete("/chats/{id}")
def delete_chat_by_id():
    pass