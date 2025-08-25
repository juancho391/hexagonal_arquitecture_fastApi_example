from kink import di
from hexagonal_arquitecture_example.application.order_service import OrderService
from hexagonal_arquitecture_example.infrastructure.fakeOrderRepository import (
    FakeOrderRepository,
)
from hexagonal_arquitecture_example.domain.fake_order_repository import (
    IFakerOrderRepository,
)
from hexagonal_arquitecture_example.infrastructure.sqlModelOrderRepository import (
    SqlModelOrderRepository,
)
from hexagonal_arquitecture_example.building_blocks.db import get_session_database


def bootstrap_setup_dependencies():
    repository = SqlModelOrderRepository(session=next(get_session_database()))
    di[IFakerOrderRepository] = repository
    di[OrderService] = OrderService(repository)
