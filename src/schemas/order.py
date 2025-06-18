from datetime import datetime
from typing import List

from pydantic import BaseModel, Field

from src.models.enums import OrderStatus
from src.schemas.dish import DishResponse


class OrderBase(BaseModel):
    customer_name: str = Field(..., min_length=1, max_length=255)


class OrderCreate(OrderBase):
    dish_ids: List[int] = Field(..., min_items=1)


class OrderStatusUpdate(BaseModel):
    status: OrderStatus


class OrderResponse(OrderBase):
    id: int
    order_time: datetime
    status: str
    dishes: List[DishResponse] = []

    class Config:
        from_attributes = True
        