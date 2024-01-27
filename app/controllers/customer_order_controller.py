from urllib import request

from flask import jsonify, request

from app.services.customer_order_service import CustomerOrderService


class CustomerOrderController:
    __customer_order_service = CustomerOrderService

    def __init__(self, _customer_order_service: CustomerOrderService = None):
        self.__customer_order_service = _customer_order_service

    def get_all_customer_order(self):
        customer_order_list = self.__customer_order_service.get_all_customer_order()
        return jsonify([customer_order.serialize() for customer_order in customer_order_list])

    def create_customer_order(self):
        try:
            data = request.json
            self.__customer_order_service.create_customer_order(data)
            return jsonify({'message': 'Customer order created successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
