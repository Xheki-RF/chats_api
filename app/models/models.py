from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
import datetime
from datetime import datetime


def get_local_time():
    return datetime.now()


class Chat(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(nullable=False, max_length=200)
    created_at: datetime = Field(default_factory=get_local_time)

    messages: list["Message"] = Relationship(back_populates="chat", cascade_delete=True)


class Message(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    chat_id: int = Field(foreign_key="chat.id", nullable=False, ondelete="CASCADE")
    text: str = Field(nullable=False, max_length=5000)
    created_at: datetime = Field(default_factory=get_local_time)

    chat: Optional[Chat] = Relationship(back_populates="messages")