from datetime import datetime


class OrderItemModel:
    instrument_name: str
    quantity: int
    price: float

    def __init__(self, instrument_name: str, quantity: int, price: float):
        self.instrument_name = instrument_name
        self.quantity = quantity
        self.price = price

    def serialize(self):
        return {
            "instrument_name": self.instrument_name,
            "quantity": self.quantity,
            "price": self.price,
        }


class CustomerOrderModel:
    id: int = 0
    customer_name: str
    delivery_address: str
    phone_number: str
    order_time: datetime
    total_price: float
    order_items: list[OrderItemModel]

    def __init__(
        self,
        id: int,
        customer_name: str,
        delivery_address: str,
        phone_number: str,
        order_time: datetime,
        total_price: float,
        order_items: list[OrderItemModel],
    ):
        self.id = id
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.phone_number = phone_number
        self.order_time = order_time
        self.total_price = total_price
        self.order_items = order_items

    def serialize(self):
        return {
            "id": self.id,
            "customer_name": self.customer_name,
            "delivery_address": self.delivery_address,
            "phone_number": self.phone_number,
            "order_time": self.order_time,
            "total_price": self.total_price,
            "order_items": [item.serialize() for item in self.order_items],
        }
