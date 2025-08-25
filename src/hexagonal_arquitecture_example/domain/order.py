from dataclasses import dataclass
from typing import Optional
from hexagonal_arquitecture_example.domain.errors import InvalidQuantityError


@dataclass
class Order:
    product_id: int
    quantity: int
    customer_id: int
    id: Optional[int] = None

    @classmethod
    def create(
        cls,
        product_id: int,
        quantity: int,
        customer_id: int,
    ) -> "Order":
        # This method create a new order and aplies the business logic
        # for example i validate the quantity is greater than 0
        if quantity <= 0:
            raise InvalidQuantityError()
        return cls(product_id=product_id, quantity=quantity, customer_id=customer_id)  # type: ignore

    @classmethod
    def create_from_db(
        cls, id: int, product_id: int, quantity: int, customer_id: int
    ) -> "Order":
        return cls(
            id=id, product_id=product_id, quantity=quantity, customer_id=customer_id
        )
