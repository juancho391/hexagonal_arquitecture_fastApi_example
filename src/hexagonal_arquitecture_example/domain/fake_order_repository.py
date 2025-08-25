from abc import ABC, abstractmethod

from hexagonal_arquitecture_example.domain.order import Order


class IFakerOrderRepository(ABC):
    @abstractmethod
    def save(self, order) -> Order: ...

    @abstractmethod
    def all(self) -> list[Order]: ...
