from typing import List
from backend.models.label import Label
from backend.models.task import Task, TaskLabel
from backend.models.users_tasks_relations import Participant_Task
from backend.schemas.task import TaskCreateDto, TaskDto
from sqlalchemy.ext.asyncio import AsyncSession


class TaskRepository:
    async def create_task(self, db: AsyncSession, task_data: TaskCreateDto) -> Task:
        new_task = Task(
            name=task_data.name
        )

        new_task.participants.extend([Participant_Task(user_id=task_data.participant, task_id=new_task.id)])
        new_task.label.extend([].append(Label(name=task_data.label.name, task_id=new_task.id)))

        db.add(new_task)

        await db.commit()
        await db.refresh(new_task)
        return new_task

    def get_tasks(self) -> List[TaskDto]:
        pass
