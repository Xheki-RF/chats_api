import app.crud.crud as crud_operations
from fastapi import FastAPI, APIRouter
from sqlmodel import Session
from app.db.db import get_session