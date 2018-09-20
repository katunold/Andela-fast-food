"""
Module to handle data storage
"""
import datetime

from flask import jsonify


class ApplicationData:
    """
        A class that contains various data structures to store data non-persistently
    """
    increment = 0

    class OrderModel:

        def __init__(self, user_name=None, order_items=None):
            self.order_id = None
            self.ordered_by = user_name
            self.order_items = order_items
            self.order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.order_status = 'pending'

    def make_order(self,  user_name, order_items):
        self.increment += 1
        current_order = self.OrderModel(user_name, order_items)
        current_order.order_id = self.increment
        new_order = {
            'order_id': current_order.order_id,
            'order_by': current_order.ordered_by,
            'order_items': current_order.order_items,
            'order_date': current_order.order_date,
            'order_status': current_order.order_status
        }

        self.orders.append(new_order)
        return self.orders

    @classmethod
    def get_orders(cls):
        return cls.orders

    @classmethod
    def find_one_order(cls, order_id):
        for order in cls.orders:
            if order_id == order['order_id']:
                return order
        return None

    @classmethod
    def update_order(cls, order_id, order_status=None):
        order = cls.find_one_order(order_id)
        if not order:
            return False
        order['order_status'] = order_status
        response_object = {
            'status': 'success',
            'message': 'Status has been updated'
        }
        return jsonify(response_object), 202

    orders = []
