from flask import Blueprint, request, jsonify
from controllers.customer_controller import CustomerController
from flask_jwt_extended import jwt_required
from __init__ import cache, limiter

customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/customers', methods=['POST'])
@jwt_required()
@limiter.limit("100 per day")
def create_customer():
    data = request.get_json()
    customer = CustomerController.create_customer(data)
    return jsonify(customer.to_dict()), 201

@customer_bp.route('/customers/<int:customer_id>', methods=['GET'])
@jwt_required()
@cache.cached(timeout=50)
@limiter.limit("100 per day")
def get_customer(customer_id):
    customer = CustomerController.get_customer_by_id(customer_id)
    if customer:
        return jsonify(customer.to_dict()), 200
    return jsonify({'message': 'Customer not found'}), 404

@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
@jwt_required()
@limiter.limit("100 per day")
def update_customer(customer_id):
    data = request.get_json()
    customer = CustomerController.update_customer(customer_id, data)
    return jsonify(customer.to_dict()), 200

@customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
@jwt_required()
@limiter.limit("100 per day")
def delete_customer(customer_id):
    CustomerController.delete_customer(customer_id)
    return jsonify({'message': 'Customer deleted'}), 200

