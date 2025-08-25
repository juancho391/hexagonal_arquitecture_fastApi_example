from sqlmodel import SQLModel, Field


class OrderModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    product_id: int
    quantity: int
    customer_id: int
