import app.crud.crud as crud_operations
from fastapi import Depends, APIRouter, Query
from sqlmodel import Session
from app.db.db import get_session
from app.schemas.schemas import Chat, CreateMessage, Message, FullChat
from typing import Annotated

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
def get_chat_by_id(id: int, limit: Annotated[int, Query(ge=1, le=100)] = 20, session: Session = Depends(get_session)) -> FullChat:
    return crud_operations.get_full_chat(id, limit, session)


# Delete chat with all messages
@chat_router.delete("/chats/{id}", status_code=204)
def delete_chat_by_id(id: int, session: Session = Depends(get_session)):
    return crud_operations.delete_chat(id, session)