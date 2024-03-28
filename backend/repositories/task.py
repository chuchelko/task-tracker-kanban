from typing import List, Sequence

from sqlalchemy.orm import subqueryload, joinedload
from sqlalchemy import select
from backend.models.comment import Comment
from backend.models.task import Task
from backend.models.users_tasks_relations import Participant_Task
from backend.repositories.user import UserRepository
from backend.schemas.task import TaskCreateDto, TaskDto, TaskUpdateDto
from sqlalchemy.ext.asyncio import AsyncSession


class TaskRepository:
    async def create_task(self, db: AsyncSession, task_data: TaskCreateDto, user_id: int, user_repository = UserRepository()) -> Task:
        new_task = Task(name=task_data.name, label_id=task_data.label_id)
        user = await user_repository.get_user_by_id(db=db, user_id=user_id)
        new_task.participants.extend(
            [Participant_Task(user_id=task_data.participant, task_id=new_task.id, name=user.name)]
        )

        db.add(new_task)

        await db.commit()
        await db.refresh(new_task)
        return new_task

    def get_tasks(self) -> List[TaskDto]:
        pass

    async def get_all_tasks_by_label_id(
        self, db: AsyncSession, label_id: int
    ) -> Sequence[Task]:
        query = await db.execute(select(Task).filter(Task.label_id == label_id))
        return query.scalars()

    async def update_task(self, db: AsyncSession, task_data: TaskUpdateDto):
        query = await db.execute(select(Task).filter(Task.id == task_data.id))
        task = query.scalar()
        if task is None:
            raise ValueError("Таска не найдена")

        if task_data.name is not None:
            task.name = task_data.name
        if task_data.label_id is not None:
            task.label_id = task_data.label_id
        if task_data.description is not None:
            task.description = task_data.description
        # if task_data.participants is not None:
        #     # умоляю работай
        #     # task.participants.extend(
        #     #     [
        #     #         Participant_Task(name=p.name, user_id=p.id, task_id=task_data.id)
        #     #         for p in task_data.participants
        #     #     ]
        #     # )
        if task_data.comments is not None:
            # умоляю работай
            task.comments = [
                Comment(text=c.text, user_id=c.user_id, task_id=task_data.id)
                for c in task_data.comments
            ]

        await db.commit()

    async def get_task(self, db: AsyncSession, task_id: int) -> Task | None:
        query = await db.execute(
            select(Task)
            .options(joinedload(Task.participants), joinedload(Task.comments))
            .filter(Task.id == task_id)
        )
        return query.scalar()
