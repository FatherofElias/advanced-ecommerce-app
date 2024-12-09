from flask import Blueprint, request, jsonify
from controllers.customer_controller import CustomerController
from flask_jwt_extended import jwt_required, get_jwt_identity
from __init__ import cache, limiter
from models.schemas.customer_schema import CustomerSchema
from models.customer import Customer

customer_bp = Blueprint('customer_bp', __name__)
customer_schema = CustomerSchema()

def admin_required(fn):
    def wrapper(*args, **kwargs):
        current_user_id = get_jwt_identity()
        current_user = Customer.query.get(current_user_id)
        if current_user and current_user.is_admin:
            return fn(*args, **kwargs)
        else:
            return jsonify({"message": "Admin access required"}), 403
    wrapper.__name__ = fn.__name__
    return wrapper

@customer_bp.route('/customers', methods=['POST'])
@limiter.limit("100/day")
@admin_required
def create_customer():
    try:
        data = request.get_json()
        print(f"Data received: {data}")
        if not data:
            return jsonify({"message": "No input data provided"}), 400

        errors = customer_schema.validate(data)
        if errors:
            print(f"Validation errors: {errors}")
            return jsonify(errors), 422

        customer = CustomerController.create_customer(data)
        print(f"Customer created: {customer.to_dict()}")
        cache.delete_memoized(list_customers)  # Clear cache on create
        return jsonify(customer.to_dict()), 201
    except Exception as e:
        print(f"Error during customer creation: {e}")
        return jsonify({"message": str(e)}), 500

@customer_bp.route('/customers/<int:customer_id>', methods=['GET'])
@limiter.limit("100/day")
@admin_required
@cache.cached(timeout=60, key_prefix='customer_<int:customer_id>')
def get_customer(customer_id):
    customer = CustomerController.get_customer_by_id(customer_id)
    if customer:
        return jsonify(customer.to_dict()), 200
    return jsonify({'message': 'Customer not found'}), 404

@customer_bp.route('/customers/<int:customer_id>', methods=['PUT'])
@limiter.limit("100/day")
@admin_required
def update_customer(customer_id):
    try:
        data = request.get_json()
        customer = CustomerController.update_customer(customer_id, data)
        if customer:
            cache.delete_memoized(get_customer, customer_id)  # Clear cache on update
            return jsonify(customer.to_dict()), 200
        return jsonify({'message': 'Customer not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@customer_bp.route('/customers/<int:customer_id>', methods=['DELETE'])
@limiter.limit("100/day")
@admin_required
def delete_customer(customer_id):
    try:
        CustomerController.delete_customer(customer_id)
        cache.delete_memoized(get_customer, customer_id)  # Clear cache on delete
        cache.delete_memoized(list_customers)  # Clear cache on delete
        return jsonify({'message': 'Customer deleted'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@customer_bp.route('/customers', methods=['GET'])
@limiter.limit("100/day")
@admin_required
@cache.cached(timeout=60, key_prefix='all_customers')
def list_customers():
    customers = CustomerController.list_customers()
    return jsonify([customer.to_dict() for customer in customers]), 200
