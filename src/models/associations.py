from sqlalchemy import Column, ForeignKey, Integer, Table

from src.database.base import Base

order_dish_association = Table(
    "order_dishes",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.id"), primary_key=True),
    Column("dish_id", Integer, ForeignKey("dishes.id"), primary_key=True),
)
