from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from src.database import async_session_factory
from src.repositories.dish import DishRepository
from src.repositories.order import OrderRepository


class UnitOfWork:
    def __init__(self, session: AsyncSession):
        self.session = session
        self.dishes = DishRepository(session)
        self.orders = OrderRepository(session)

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            await self.rollback()
        await self.session.close()


async def get_uow() -> AsyncGenerator[UnitOfWork, None]:
    async with async_session_factory() as session:
        yield UnitOfWork(session)
