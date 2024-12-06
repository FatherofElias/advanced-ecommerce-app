from flask import Blueprint, request, jsonify
from controllers.customer_controller import CustomerController
from flask_jwt_extended import jwt_required

customer_bp = Blueprint('customer_bp', __name__)

@customer_bp.route('/customers', methods=['POST'])
@jwt_required()
def create_customer():
    data = request.get_json()
    customer = CustomerController.create_customer(data)
    return jsonify(customer.to_dict()), 201

@customer_bp.route('/customers/<int:customer_id>', methods=['GET'])
@jwt_required()
def get_customer(customer_id):
    customer = CustomerController.get_customer_by_id(customer_id)
    return jsonify(customer.to_dict()), 200

@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
@jwt_required()
def update_customer(customer_id):
    data = request.get_json()
    customer = CustomerController.update_customer(customer_id, data)
    return jsonify(customer.to_dict()), 200

@customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
@jwt_required()
def delete_customer(customer_id):
    CustomerController.delete_customer(customer_id)
    return jsonify({'message': 'Customer deleted'}), 200
