from fastapi import FastAPI, Depends
from hexagonal_arquitecture_example.application.dto import CreateOrderDto, OrderDto
from hexagonal_arquitecture_example.application.order_service import OrderService
from hexagonal_arquitecture_example.infrastructure.fakeOrderRepository import (
    FakeOrderRepository,
)
from hexagonal_arquitecture_example.domain.fake_order_repository import (
    IFakerOrderRepository,
)
from hexagonal_arquitecture_example.controller import router as order_router
from fastapi.openapi.utils import get_openapi
from typing import Any
from fastapi.middleware.cors import CORSMiddleware
from hexagonal_arquitecture_example.building_blocks.db import init_db


app = FastAPI()

init_db()
# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(order_router)


def custom_openapi() -> dict[str, Any]:
    if app.openapi_schema:
        return app.openapi_schema  # type: ignore

    openapi_schema = get_openapi(
        title="hexagonal-architecture-python",
        version="1.0.0",
        description="Hexagonal architecture in Python build on top of FastAPI",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema  # type: ignore


app.openapi = custom_openapi
