from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from hexagonal_arquitecture_example.application.dto import CreateOrderDto, OrderDto
from hexagonal_arquitecture_example.application.order_service import OrderService
from kink import di

from hexagonal_arquitecture_example.domain.errors import InvalidQuantityError

router = APIRouter()


@router.post("/orders/", response_model=OrderDto)
async def create_order(
    order: CreateOrderDto,
    order_service: OrderService = Depends(lambda: di[OrderService]),
) -> JSONResponse:
    try:
        new_order = order_service.create(order=order)
    except InvalidQuantityError as error:
        raise HTTPException(status_code=400, detail=str(error))
    return JSONResponse(
        content=new_order.model_dump(), status_code=status.HTTP_201_CREATED
    )


@router.get("/orders/", response_model=list[OrderDto], status_code=status.HTTP_200_OK)
async def get_orders(
    order_service: OrderService = Depends(lambda: di[OrderService]),
) -> list[OrderDto]:
    orders = order_service.getOrders()
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found")
    return orders
