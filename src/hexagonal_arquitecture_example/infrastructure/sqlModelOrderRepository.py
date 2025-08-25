from sqlmodel import SQLModel, create_engine, Session, select
from hexagonal_arquitecture_example.domain.order import Order
from hexagonal_arquitecture_example.domain.fake_order_repository import (
    IFakerOrderRepository,
)
from fastapi import Depends
from hexagonal_arquitecture_example.domain.order import Order
from hexagonal_arquitecture_example.application.dto import OrderDto, CreateOrderDto
from hexagonal_arquitecture_example.infrastructure.models.order_model import OrderModel


class SqlModelOrderRepository(IFakerOrderRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def save(self, order: Order) -> Order:
        order_model = OrderModel.model_validate(CreateOrderDto(**order.__dict__))
        self.session.add(order_model)
        self.session.commit()
        self.session.refresh(order_model)
        return Order.create_from_db(**order_model.model_dump())

    def all(self) -> list[Order]:
        orders_db = self.session.exec(select(OrderModel)).all()
        return [Order(**order.model_dump()) for order in orders_db]
