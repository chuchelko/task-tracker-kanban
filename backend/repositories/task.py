from typing import List
from backend.models.task import Task
from backend.schemas.task import TaskDto
from sqlalchemy.ext.asyncio import AsyncSession
from backend.models import User


class TaskRepository:
    async def create_task(self, db: AsyncSession, task_data: TaskDto) -> User:
        new_task = Task(name = task_data.name)
        db.add(new_task)
        await db.commit()
        await db.refresh(new_task)
        return new_task
    
    def get_tasks(self) -> List[TaskDto]:
        pass