from typing import Annotated, Union, Counter

from fastapi import APIRouter, Depends, Query

from repo import RepoTask
from shemas import TaskADD, Task, ErrorResponse, CounterTask

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

@router.get("/count/col", summary="Количество выполненных заданий", description="Получение количества выполненных заданий в базе данных")
async def get_count_completed() -> dict[str , str]:
    count = await RepoTask.count_tasks()
    return {"answer": f"В базе данных {count} выполненных заданий"}

@router.delete("/by-name/name" , summary="Удаление по имени", description="Удаление задания по названию")
async def delete_task_by_name(name: str) -> Union[ErrorResponse, dict[str, bool]]:
    result = await RepoTask.delete_task_by_name(name)
    if not result:
        return ErrorResponse(ok=False, message="Task not found")
    return {"ok": True}

@router.put("/{task_id}/done", summary="Отметить задание как выполненное", description="Отметить задание как выполненное")
async def mark_task_done(task_id: int) -> Union[ErrorResponse, dict[str, bool]]:
    result = await RepoTask.mark_task_done(task_id)
    if not result:
        return ErrorResponse(ok=False, message="Task not found")
    return {"ok": True}








