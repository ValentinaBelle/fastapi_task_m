# работаем с базой данных как с коллекцией объектов
from database import new_session, TaskOrm
from main import STaskAdd


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd):
        async with new_session() as session:  # открывшийся контекстный менеджер отдает объект сессии
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.flush()  # отправит сообщение в базу, получит id и присвоит ключ task
            await session.commit()
            return task.id


    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            return task_models
