import pytest
from hexagonal_arquitecture_example.infrastructure.sqlModelOrderRepository import (
    SqlModelOrderRepository,
)
from tests.conftest import get_session_test_db
from hexagonal_arquitecture_example.domain.order import Order


def test_sql_model_repository_save():
    repo = SqlModelOrderRepository(session=next(get_session_test_db()))
    order = Order.create(product_id=1, quantity=5, customer_id=10)

    save_order = repo.save(order=order)

    assert isinstance(save_order, Order)


def test_sql_model_repository_all():
    repo = SqlModelOrderRepository(session=next(get_session_test_db()))
    order1 = Order.create(product_id=1, quantity=5, customer_id=10)

    repo.save(order1)

    all_orders = repo.all()

    assert len(all_orders) == 1
