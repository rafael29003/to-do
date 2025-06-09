from sqlalchemy import select, delete, func, update

from database import new_session, TaskTabel
from shemas import TaskADD, Task


class RepoTask:
    @classmethod
    async def add_one(cls  , data : TaskADD):
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskTabel(**task_dict)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    @classmethod
    async def get_tasks(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskTabel)
            result = await session.execute(query)
            task_models = result.scalars().all()
            task_shemas = [Task.model_validate(task_model) for task_model in task_models]
            return task_shemas
    
    @classmethod
    async def get_task_by_id(cls, task_id: int) -> Task | None:
        async with new_session() as session:
            query = select(TaskTabel).where(TaskTabel.id == task_id)
            result = await session.execute(query)
            task_model = result.scalar_one_or_none()
            return Task.model_validate(task_model.__dict__) if task_model else None
    
    @classmethod
    async def delete_task(cls, task_id: int) -> bool:
        async with new_session() as session:
            query = delete(TaskTabel).where(TaskTabel.id == task_id)
            result = await session.execute(query)
            await session.commit()
            return result.rowcount > 0
    
    @classmethod
    async def count_tasks(cls) -> int:
        async with new_session() as session:
            query = select(func.count()).select_from(TaskTabel)
            result = await session.execute(query)
            count = result.scalar_one()
            return count
    
    @classmethod
    async def delete_task_by_name(cls, name: str) -> bool:
        async with new_session() as session:
            query = delete(TaskTabel).where(TaskTabel.name == name)
            result = await session.execute(query)
            await session.commit()
            return result.rowcount > 0

    @classmethod
    async def mark_task_done(cls, task_id):
        async with new_session() as session:
            query = update(TaskTabel).where(TaskTabel.id == task_id).values(done=True)
            result = await session.execute(query)
            await session.commit()
            return result.rowcount > 0







