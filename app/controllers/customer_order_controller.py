from urllib import request

from flask import jsonify, request

from app.services.customer_order_service import CustomerOrderService


class CustomerOrderController:
    __customer_order_service = CustomerOrderService

    def __init__(self, _customer_order_service: CustomerOrderService = None):
        self.__customer_order_service = _customer_order_service

    def get_all_customer_order(self):
        data_params = request.args
        customer_order_list = self.__customer_order_service.get_all_customer_order(data_params)
        return jsonify([customer_order.serialize() for customer_order in customer_order_list])

    def create_customer_order(self):
        try:
            data = request.json
            self.__customer_order_service.create_customer_order(data)
            return jsonify({'message': 'Customer order created successfully'})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    # def get_customer_order_by_phone_number(self, phone_number):
    #     try:
    #         customer_order = self.__customer_order_service.get_customer_order_by_phone_number(phone_number)
    #         return jsonify(customer_order.serialize())
    #     except Exception as e:
    #         return jsonify({'error': str(e)}), 500
