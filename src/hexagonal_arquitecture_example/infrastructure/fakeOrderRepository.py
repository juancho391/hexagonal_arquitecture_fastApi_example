from hexagonal_arquitecture_example.domain.fake_order_repository import (
    IFakerOrderRepository,
)

from hexagonal_arquitecture_example.domain.order import Order


class FakeOrderRepository(IFakerOrderRepository):
    def __init__(self) -> None:
        self.orders = []

    def save(self, order: Order) -> Order:
        self.orders.append(order)
        return order

    def all(self) -> list[Order]:
        return self.orders
