from datetime import datetime

from app.models.customer_order_model import CustomerOrderModel, OrderItemModel
from app.models.models import CustomerOrder, OrderItem
from app.repositories.customer_order_repository import CustomerOrderRepository
from app.repositories.instrument_item_repository import InstrumentItemRepository


class CustomerOrderService:
    __customer_order_repository: CustomerOrderRepository
    __instrument_item_repository: InstrumentItemRepository

    def __init__(
        self,
        _customer_order_repository=None,
        _instrument_item_repository=None,
    ):
        self.__customer_order_repository = _customer_order_repository
        self.__instrument_item_repository = _instrument_item_repository

    def get_all_customer_order(self, data) -> list[CustomerOrderModel]:
        return [
            CustomerOrderModel(
                id=entity.id,
                customer_name=entity.customer_name,
                order_time=entity.order_time,
                delivery_address=entity.delivery_address,
                phone_number=entity.phone_number,
                total_price=entity.total_price,
                order_items=[
                    OrderItemModel(
                        instrument_name=item.instrument_item.instrument.instrument_name,
                        quantity=item.quantity,
                        price=item.price,
                    )
                    for item in entity.order_items
                ],
            )
            for entity in self.__customer_order_repository.get(data)
        ]

    def create_customer_order(self, data):
        customer_name = data.get("customer_name")
        delivery_address = data.get("delivery_address")
        phone_number = data.get("phone_number")
        order_items = data.get("orders", [])
        items: list[OrderItem] = []

        total_price = 0
        current_datetime = datetime.now()
        for order_item in order_items:
            instrument_id = order_item.get("id")
            quantity = order_item.get("quantity")
            instrument_item = self.__instrument_item_repository.get_by_id(instrument_id)
            total_price += instrument_item.price * quantity
            items.append(
                OrderItem(
                    instrument_item=instrument_item,
                    quantity=quantity,
                    price=instrument_item.price,
                )
            )
        return self.__customer_order_repository.create(
            CustomerOrder(
                customer_name=customer_name,
                delivery_address=delivery_address,
                phone_number=phone_number,
                total_price=total_price,
                order_time=current_datetime,
                order_items=items,
            )
        )

    def get_customer_order_by_phone_number(self, phone_number):
        return self.__customer_order_repository.get_by_phone_number(
            phone_number=phone_number
        )
