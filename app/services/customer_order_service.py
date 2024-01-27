from datetime import datetime

from app.models.customer_order_model import CustomerOrderModel
from app.models.models import CustomerOrder, OrderItem
from app.repositories.customer_order_repository import CustomerOrderRepository
from app.repositories.instrument_item_repository import InstrumentItemRepository


class CustomerOrderService:
    __customer_order_repository: CustomerOrderRepository
    __instrument_item_repository: InstrumentItemRepository

    def __init__(self, _customer_order_repository=None, _instrument_item_repository=None):
        self.__customer_order_repository = _customer_order_repository
        self.__instrument_item_repository = _instrument_item_repository

    def get_all_customer_order(self) -> list[CustomerOrderModel]:
        return [CustomerOrderModel(entity.id, entity.customer_id, entity.order_date, entity.order_status) for entity in
                self.__customer_order_repository.get_all()]

    def create_customer_order(self, data):
        customer_name = data.get('customer_name')
        delivery_address = data.get('delivery_address')
        phone_number = data.get('phone_number')
        order_items = data.get('orders', [])
        items: list[OrderItem] = []

        total_price = 0
        current_datetime = datetime.now()
        for order_item in order_items:
            instrument_id = order_item.get('id')
            quantity = order_item.get('quantity')
            instrument_item = self.__instrument_item_repository.get_by_id(instrument_id)
            total_price += instrument_item.price * quantity
            items.append(OrderItem(instrument_item=instrument_item, quantity=quantity, price=instrument_item.price))
        return self.__customer_order_repository.create(
            CustomerOrder(customer_name=customer_name, delivery_address=delivery_address, phone_number=phone_number,
                          total_price=total_price, order_time=current_datetime, order_items=items))
