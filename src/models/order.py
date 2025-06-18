"""Order model."""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String(255), nullable=False)
    order_time = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    status = Column(String(50), nullable=False, default="в обработке")
    
    dishes = relationship("Dish", secondary="order_dishes", back_populates="orders")

    def __repr__(self) -> str:
        return f"<Order(id={self.id}, customer='{self.customer_name}', status='{self.status}')>"
    