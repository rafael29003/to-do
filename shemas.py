from pydantic import BaseModel


class TaskADD(BaseModel):
    name: str
    description: str | None = None


class Task(TaskADD):
    id: int


class ErrorResponse(BaseModel):
    ok: bool
    message: str

class CounterTask(BaseModel):
    answer : str


