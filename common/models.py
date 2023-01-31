from dataclasses import dataclass
from datetime import datetime


@dataclass
class Product:
    price: float
    name: str
    discount: int
    description: str
    delivery_date: str
    producer: str

    def __init__(
        self,
        price: float = None,
        name: str = "",
        discount: int = 0,
        producer: str = None,
        description: str = None,
        delivery_date: str = None,
    ) -> None:
        self.price = price
        self.name = name
        self.discount = discount
        self.producer = producer
        self.description = description
        self.delivery_date = delivery_date
