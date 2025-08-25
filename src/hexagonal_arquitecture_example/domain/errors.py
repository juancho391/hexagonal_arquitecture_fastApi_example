class DomainError(Exception):
    pass


class InvalidQuantityError(DomainError):
    def __init__(self):
        super().__init__("Invalid quantity,it must be greater than 0")
