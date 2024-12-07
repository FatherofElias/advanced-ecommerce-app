from flask import Blueprint, request, jsonify
from controllers.product_controller import ProductController
from flask_jwt_extended import jwt_required
from __init__ import cache, limiter

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['POST'])
@jwt_required()
@limiter.limit("100 per day")
def create_product():
    data = request.get_json()
    product = ProductController.create_product(data)
    return jsonify(product.to_dict()), 201

@product_bp.route('/products/<int:product_id>', methods=['GET'])
@jwt_required()
@cache.cached(timeout=50)
@limiter.limit("100 per day")
def get_product(product_id):
    product = ProductController.get_product_by_id(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    return jsonify({'message': 'Product not found'}), 404

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
@limiter.limit("100 per day")
def update_product(product_id):
    data = request.get_json()
    product = ProductController.update_product(product_id, data)
    return jsonify(product.to_dict()), 200

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
@limiter.limit("100 per day")
def delete_product(product_id):
    ProductController.delete_product(product_id)
    return jsonify({'message': 'Product deleted'}), 200

@product_bp.route('/products', methods=['GET'])
@jwt_required()
@cache.cached(timeout=50)
@limiter.limit("100 per day")
def list_products():
    products = ProductController.list_products()
    return jsonify([product.to_dict() for product in products]), 200
