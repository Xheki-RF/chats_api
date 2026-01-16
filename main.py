from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from app.db.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

if __name__ == "__main__":
    uvicorn.run(app="main:app", reload=True)