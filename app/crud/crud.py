import app.schemas.schemas as schemas
from sqlmodel import Session, select
from app.models.models import Chat, Message


def create_chat(title: schemas.CreateChat, session: Session) -> schemas.Chat:
    new_chat = Chat(**title.model_dump())

    session.add(new_chat)
    session.commit()
    session.refresh(new_chat)

    return new_chat


def create_message(id: int, text: schemas.CreateMessage, session: Session) -> schemas.Message:
    new_message = Message(chat_id=id, text=text)

    session.add(new_message)
    session.commit()
    session.refresh(new_message)

    return new_message