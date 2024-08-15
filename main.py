from typing import Optional, Annotated
from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("The base is clear")
    await create_tables()  # создает таблицы при старте приложения
    print("The base is ready")
    yield
    print("The program exists")


app = FastAPI(lifespan=lifespan)


class STaskAdd(BaseModel):
    name: str
    description: str | None


class STask(STaskAdd):  # наследует от STaskAdd
    id: int  # id - первичный ключ в базе данных


tasks = []


