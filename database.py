from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped
from sqlalchemy.testing.schema import mapped_column


engine = create_async_engine("sqlite+aiosqlite:///tasks.db")

new_session = async_sessionmaker(engine , expire_on_commit=False)

class Model(DeclarativeBase):
    pass


class TaskTabel(Model):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    done: Mapped[bool] = mapped_column(default=False)
    name: Mapped[str] = mapped_column()
    description: Mapped[str | None] = mapped_column(nullable=True)


async def create_table():
    async with engine.begin() as conn:
        await  conn.run_sync(Model.metadata.create_all)

async def delete_table():
    async with engine.begin() as conn:
        await  conn.run_sync(Model.metadata.drop_all)









