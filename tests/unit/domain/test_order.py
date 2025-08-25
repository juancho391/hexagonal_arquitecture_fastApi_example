import pytest
from hexagonal_arquitecture_example.domain.order import Order
from hexagonal_arquitecture_example.domain.errors import InvalidQuantityError


def test_create_order_success():
    order = Order.create(product_id=1, quantity=5, customer_id=10)
    assert order.product_id == 1
    assert order.quantity == 5
    assert order.customer_id == 10


def test_create_order_with_invalid_quantity():
    with pytest.raises(
        InvalidQuantityError, match="Invalid quantity,it must be greater than 0"
    ):
        Order.create(product_id=1, quantity=0, customer_id=10)
