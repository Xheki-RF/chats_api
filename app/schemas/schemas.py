from pydantic import BaseModel, field_validator, model_validator, Field
from typing import Optional
from datetime import datetime


class CreateChat(BaseModel):
    title: str = Field(min_length=1, max_length=200)

    @field_validator("title")
    def title_check(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("title was not provided")
        else:
            return value
        

class Chat(CreateChat):
    id: int
    created_at: datetime


class CreateMessage(BaseModel):
    text: str = Field(min_length=1, max_length=5000)

    @field_validator("text")
    def text_check(cls, value):
        value = value.strip()

        if not value:
            raise ValueError("text was not provided")
        else:
            return value


class Message(CreateMessage):
    id: int
    chat_id: int
    created_at: datetime
