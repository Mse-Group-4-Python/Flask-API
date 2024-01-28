from datetime import datetime


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

    def serialize(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'delivery_address': self.delivery_address,
            'phone_number': self.phone_number,
            'order_time': self.order_time,
            'total_price': self.total_price
        }
