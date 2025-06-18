from pydantic import BaseModel, Field


class DishBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    category: str = Field(..., min_length=1, max_length=100)


class DishCreate(DishBase):
    pass


class DishResponse(DishBase):
    id: int

    class Config:
        from_attributes = True
        