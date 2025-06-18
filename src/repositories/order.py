from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from src.models import Order
from src.repositories.base import BaseRepository
from src.schemas.order import OrderCreate


class OrderRepository(BaseRepository[Order, OrderCreate, None]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Order)

    async def get_with_dishes(self, id: int) -> Optional[Order]:
        result = await self.session.execute(
            select(self.model)
            .options(selectinload(self.model.dishes))
            .where(self.model.id == id)
        )
        return result.scalar_one_or_none()

    async def get_all_with_dishes(self) -> List[Order]:
        result = await self.session.execute(
            select(self.model).options(selectinload(self.model.dishes))
        )
        return list(result.scalars().all())

    async def update_status(self, order: Order, status: str) -> Order:
        order.status = status
        await self.session.flush()
        await self.session.refresh(order)
        return order
