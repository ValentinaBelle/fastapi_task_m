from typing import Optional, Annotated
from fastapi import APIRouter

from main import STaskAdd
from repository import TaskRepository

router = APIRouter()
prefix = "/tasks"


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {"tasks": tasks}
