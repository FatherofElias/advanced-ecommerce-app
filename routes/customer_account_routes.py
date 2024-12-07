import functools
from flask import Blueprint, request, jsonify
from controllers.customer_controller import CustomerController
from flask_jwt_extended import jwt_required
from __init__ import cache, limiter
from utils.jwt_utils import get_current_user

account_bp = Blueprint('account_bp', __name__)

def admin_required(fn):
    @functools.wraps(fn)
    @jwt_required()
    def wrapper(*args, **kwargs):
        user = get_current_user()
        if user['role'] != 'admin':
            return jsonify({'message': 'Admin access required'}), 403
        return fn(*args, **kwargs)
    return wrapper

@account_bp.route('/customer_accounts', methods=['POST'])
@admin_required
@limiter.limit("100 per day")
def create_customer_account():
    data = request.get_json()
    account = CustomerController.create_customer_account(data)
    return jsonify(account.to_dict()), 201

@account_bp.route('/customer_accounts/<int:account_id>', methods=['GET'])
@admin_required
@cache.cached(timeout=50)
@limiter.limit("100 per day")
def get_customer_account(account_id):
    account = CustomerController.get_customer_account_by_id(account_id)
    if account:
        return jsonify(account.to_dict()), 200
    return jsonify({'message': 'Customer account not found'}), 404

@account_bp.route('/customer_accounts/<int:account_id>', methods=['PUT'])
@admin_required
@limiter.limit("100 per day")
def update_customer_account(account_id):
    data = request.get_json()
    account = CustomerController.update_customer_account(account_id, data)
    return jsonify(account.to_dict()), 200

@account_bp.route('/customer_accounts/<int:account_id>', methods=['DELETE'])
@admin_required
@limiter.limit("100 per day")
def delete_customer_account(account_id):
    CustomerController.delete_customer_account(account_id)
    return jsonify({'message': 'Customer account deleted'}), 200
