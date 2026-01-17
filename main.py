from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from app.db.db import init_db
from app.api.api_endpoints import chat_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", port=8000, reload=True)

app.include_router(chat_router)
