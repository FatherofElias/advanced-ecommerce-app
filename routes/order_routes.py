from flask import Blueprint, request, jsonify
from controllers.order_controller import OrderController
from flask_jwt_extended import jwt_required
from __init__ import cache, limiter

order_bp = Blueprint('order_bp', __name__)

@order_bp.route('/orders', methods=['POST'])
@jwt_required()
@limiter.limit("100 per day")
def create_order():
    data = request.get_json()
    order = OrderController.create_order(data)
    return jsonify(order.to_dict()), 201

@order_bp.route('/orders/<int:order_id>', methods=['GET'])
@jwt_required()
@cache.cached(timeout=50)
@limiter.limit("100 per day")
def get_order(order_id):
    order = OrderController.get_order_by_id(order_id)
    if order:
        return jsonify(order.to_dict()), 200
    return jsonify({'message': 'Order not found'}), 404
