from hexagonal_arquitecture_example.domain.fake_order_repository import (
    IFakerOrderRepository,
)
from .dto import CreateOrderDto, OrderDto
from kink import inject
from hexagonal_arquitecture_example.domain.order import Order


@inject
class OrderService:
    def __init__(self, order_repository: IFakerOrderRepository) -> None:
        self._order_repository = order_repository

    def create(self, order: CreateOrderDto) -> OrderDto:
        order_domain = Order.create(
            product_id=order.product_id,
            quantity=order.quantity,
            customer_id=order.customer_id,
        )

        new_order = self._order_repository.save(order=order_domain)
        return OrderDto(**new_order.__dict__)

    def getOrders(self) -> list[OrderDto]:
        orders = self._order_repository.all()
        return [OrderDto(**order.__dict__) for order in orders]
