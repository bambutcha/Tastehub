"""Dish model."""

from sqlalchemy import Column, Float, Integer, String, Text

from src.database.base import Base


class Dish(Base):
    """Блюдо в меню."""
    
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)

    def __repr__(self) -> str:
        return f"<Dish(id={self.id}, name='{self.name}', price={self.price})>"
    