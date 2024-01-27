from datetime import datetime
from typing import Optional


class CustomerOrderModel:
    id: int = 0
    customer_name: str
    delivery_address: str
    phone_number: str
    order_time: datetime
    total_price: float

    def __init__(self, id: int, customer_name: str, delivery_address: str, phone_number: str, order_time: datetime,
                    total_price: float):
            self.id = id
            self.customer_name = customer_name
            self.delivery_address = delivery_address
            self.phone_number = phone_number
            self.order_time = order_time
            self.total_price = total_price