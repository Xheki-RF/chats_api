import app.schemas.schemas as schemas
from sqlmodel import Session, select
from app.models.models import Chat, Message
from sqlalchemy import desc
from fastapi import HTTPException


def create_chat(title: schemas.CreateChat, session: Session) -> schemas.Chat:
    new_chat = Chat(**title.model_dump())

    session.add(new_chat)
    session.commit()
    session.refresh(new_chat)

    return new_chat


def create_message(id: int, text: schemas.CreateMessage, session: Session) -> schemas.Message:
    get_chat = session.exec(select(Chat).where(Chat.id == id)).first()

    if not get_chat:
        raise HTTPException(404)
    
    new_message = Message(chat_id=id, text=text.text)

    session.add(new_message)
    session.commit()
    session.refresh(new_message)

    return new_message


def get_full_chat(id: int, limit: int, session: Session) -> schemas.FullChat:
    chat_select = session.exec(select(Chat).where(Chat.id == id)).first()

    if not chat_select:
        raise HTTPException(404)

    messages_select = session.exec(select(Message).where(Message.chat_id == id).order_by(desc(Message.created_at)).limit(limit)).all()

    return schemas.FullChat(chat=chat_select, messages=messages_select)


def delete_chat(id: int, sesion: Session):
    chat = sesion.exec(select(Chat).where(Chat.id == id)).first()

    if not chat:
        raise HTTPException(404)

    sesion.delete(chat)
    sesion.commit()