from flask import Blueprint, request, jsonify
from controllers.customer_controller import CustomerController
from flask_jwt_extended import jwt_required

account_bp = Blueprint('account_bp', __name__)

@account_bp.route('/customer_accounts', methods=['POST'])
@jwt_required()
def create_customer_account():
    data = request.get_json()
    account = CustomerController.create_customer_account(data)
    return jsonify(account.to_dict()), 201

@account_bp.route('/customer_accounts/<int:account_id>', methods=['GET'])
@jwt_required()
def get_customer_account(account_id):
    account = CustomerController.get_customer_account_by_id(account_id)
    return jsonify(account.to_dict()), 200

@account_bp.route('/customer_accounts/<int:account_id>', methods=['PUT'])
@jwt_required()
def update_customer_account(account_id):
    data = request.get_json()
    account = CustomerController.update_customer_account(account_id, data)
    return jsonify(account.to_dict()), 200

@account_bp.route('/customer_accounts/<int:account_id>', methods=['DELETE'])
@jwt_required()
def delete_customer_account(account_id):
    CustomerController.delete_customer_account(account_id)
    return jsonify({'message': 'Customer account deleted'}), 200
