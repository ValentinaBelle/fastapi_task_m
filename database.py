from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
# добавляем из расширения asyncio добавляем асинхронный движок для работы с базами данных


# асинхронный движок отправляет запросы в базу данных
engine = create_async_engine("sqlite+aiosqlite://tasks.db")

new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class TaskOrm(Model):  # can be TaskTable though
    __tablename__ = "tasks"

    # необходим первичный ключ, чтобы sqlalchemy дал создать таблицу
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]


# асинхронная функция для создания таблиц
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)

# асинхронная функция для удаления таблиц в данном проекте
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)