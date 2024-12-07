from models import db
from models.product import Product

class ProductService:
    @staticmethod
    def create_product(data):
        product = Product(name=data['name'], price=data['price'])
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def update_product(product_id, data):
        product = Product.query.get(product_id)
        if product:
            product.name = data.get('name', product.name)
            product.price = data.get('price', product.price)
            db.session.commit()
        return product

    @staticmethod
    def delete_product(product_id):
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
        return product

    @staticmethod
    def list_products():
        return Product.query.all()
