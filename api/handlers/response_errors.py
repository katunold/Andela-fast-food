"""
Module to handle all error responses
"""
from flask import jsonify


class ResponseErrors:
    """
        Error handler to handle response errors.
        """

    @staticmethod
    def invalid_data_format():
        response_object = {
            'status': 'fail',
            'error_message': 'Please use character strings',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def empty_data_fields():
        response_object = {
            'status': 'fail',
            'error_message': 'Some fields have no data',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def empty_data_storage():
        response_object = {
            'status': 'success',
            'message': 'No orders currently',
            'data': False
        }
        return jsonify(response_object), 200

    @staticmethod
    def order_absent():
        response_object = {
            'status': 'fail',
            'error_message': 'Order does not exist',
            'data': False
        }
        return jsonify(response_object), 400

    @staticmethod
    def missing_key(keys):
        response_object = {
            'status': 'fail',
            'error_message': 'Missing key ' + keys,
            'data': False
        }
        return jsonify(response_object), 400
