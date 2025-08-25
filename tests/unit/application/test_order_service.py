import pytest
from hexagonal_arquitecture_example.domain.fake_order_repository import (
    IFakerOrderRepository,
)
from hexagonal_arquitecture_example.infrastructure.sqlModelOrderRepository import (
    SqlModelOrderRepository,
)
from hexagonal_arquitecture_example.application.order_service import OrderService
from hexagonal_arquitecture_example.application.dto import CreateOrderDto, OrderDto
from hexagonal_arquitecture_example.domain.order import Order
from hexagonal_arquitecture_example.infrastructure.sqlModelOrderRepository import (
    SqlModelOrderRepository,
)
from tests.conftest import get_session_test_db


def test_create_and_save_order_success():
    fake_repo = SqlModelOrderRepository(session=next(get_session_test_db()))
    order_service = OrderService(order_repository=fake_repo)
    dto = CreateOrderDto(product_id=1, quantity=5, customer_id=15)

    result = order_service.create(dto)

    assert isinstance(result, OrderDto)
    assert result.quantity == 5
    assert result.customer_id == 15
