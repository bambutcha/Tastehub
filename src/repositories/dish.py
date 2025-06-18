from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Dish
from src.repositories.base import BaseRepository
from src.schemas.dish import DishCreate


class DishRepository(BaseRepository[Dish, DishCreate, None]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Dish)

    async def get_by_ids(self, dish_ids: List[int]) -> List[Dish]:
        result = await self.session.execute(
            select(self.model).where(self.model.id.in_(dish_ids))
        )
        return list(result.scalars().all())
