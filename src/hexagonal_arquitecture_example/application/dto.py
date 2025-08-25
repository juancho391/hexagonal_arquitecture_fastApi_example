from sqlmodel import SQLModel


class CreateOrderDto(SQLModel):
    product_id: int
    quantity: int
    customer_id: int


class OrderDto(SQLModel):
    id: int
    product_id: int
    quantity: int
    customer_id: int
