from flask import Blueprint, request, jsonify
from controllers.product_controller import ProductController
from flask_jwt_extended import jwt_required, get_current_user
from __init__ import cache, limiter
from models.schemas.product_schema import ProductSchema

product_bp = Blueprint('product_bp', __name__)
product_schema = ProductSchema()

@product_bp.route('/products', methods=['POST'])
@jwt_required()
@limiter.limit("100/day")
def create_product():
    user_identity = get_current_user()
    print(f"User identity: {user_identity}")  

    data = request.get_json()
    if not data:
        return jsonify({"message": "No input data provided"}), 400

    errors = product_schema.validate(data)
    if errors:
        return jsonify(errors), 422

    product = ProductController.create_product(data)
    cache.delete_memoized(list_products) 
    return jsonify(product.to_dict()), 201


@product_bp.route('/products/<int:product_id>', methods=['GET'])
@jwt_required()
@limiter.limit("100/day")
@cache.cached(timeout=60, key_prefix='product_<int:product_id>')
def get_product(product_id):
    product = ProductController.get_product_by_id(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    return jsonify({'message': 'Product not found'}), 404

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
@limiter.limit("100/day")
def update_product(product_id):
    try:
        data = request.get_json()
        product = ProductController.update_product(product_id, data)
        if product:
            cache.delete_memoized(get_product, product_id)  
            return jsonify(product.to_dict()), 200
        return jsonify({'message': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
@limiter.limit("100/day")
def delete_product(product_id):
    try:
        ProductController.delete_product(product_id)
        cache.delete_memoized(get_product, product_id)  
        cache.delete_memoized(list_products)  
        return jsonify({'message': 'Product deleted'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@product_bp.route('/products', methods=['GET'])
@jwt_required()
@limiter.limit("100/day")
@cache.cached(timeout=60, key_prefix='all_products')
def list_products():
    products = ProductController.list_products()
    return jsonify([product.to_dict() for product in products]), 200
