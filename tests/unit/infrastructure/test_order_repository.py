import pytest
from hexagonal_arquitecture_example.infrastructure.fakeOrderRepository import (
    FakeOrderRepository,
)
from hexagonal_arquitecture_example.domain.order import Order


def test_fake_order_repository_save():
    repo = FakeOrderRepository()
    order = Order.create(product_id=1, quantity=5, customer_id=10)

    save_order = repo.save(order=order)

    assert save_order == order
    assert len(repo.orders) == 1


def test_fake_order_repository_all():
    repo = FakeOrderRepository()
    order1 = Order.create(product_id=1, quantity=5, customer_id=10)
    order2 = Order.create(product_id=2, quantity=3, customer_id=20)

    repo.save(order1)
    repo.save(order2)

    all_orders = repo.all()

    assert len(all_orders) == 2
    assert all_orders[0] == order1
    assert all_orders[1] == order2
