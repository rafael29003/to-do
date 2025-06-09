from typing import Annotated, Union

from fastapi import APIRouter, Depends, Query

from repo import RepoTask
from shemas import TaskADD, Task, ErrorResponse

router = APIRouter(
    prefix="/tasks",
    tags=["Задания"],
)

@router.post("", summary="Добавление задания", description="Добавление задания в базу данных")
async def add_tasks(task: Annotated[TaskADD , Depends()]):
    task_id = await RepoTask.add_one(task)
    return {"ok": True , "task_id" : task_id}

@router.get("", summary="Получение всех заданий", description="Получение всех заданий из базы данных")
async def get_home() -> list[Task]:
    tasks = await RepoTask.get_tasks()
    return tasks

@router.get("/{task_id}", summary="Получение задания по ID", description="Получение задания по ID из базы данных")
async def get_task_by_id(task_id: int) -> Union[Task, ErrorResponse]:
    task = await RepoTask.get_task_by_id(task_id)
    if task == None:
        return ErrorResponse(ok=False, message="Task not found")
    else:
        return task

@router.delete("/{task_id}", summary="Удаление задания", description="Удаление задания из базы данных")
async def delete_task(task_id: int) -> Union[ErrorResponse, dict[str, bool]]:
    result = await RepoTask.delete_task(task_id)
    if not result:
        return ErrorResponse(ok=False, message="Task not found")
    return {"ok": True}

@router.get("/count", summary="Количество заданий", description="Получение количества заданий в базе данных")
async def get_count() -> str: 
    count = await RepoTask.count_tasks()
    return {"message" : f"В базе данных {count} заданий"}






