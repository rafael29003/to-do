
from contextlib import asynccontextmanager
from database import create_table , delete_table
from Router import router as router_task

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from shemas import TaskADD


@asynccontextmanager
async def lifespan(app : FastAPI):
    await delete_table()
    print("База данных очищена")
    await create_table()
    print("База данных создана")
    yield
    print("Выключение")

app = FastAPI(lifespan=lifespan)
app.include_router(router_task)