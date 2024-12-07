from services.product_service import ProductService

class ProductController:
    @staticmethod
    def create_product(data):
        return ProductService.create_product(data)

    @staticmethod
    def get_product_by_id(product_id):
        return ProductService.get_product_by_id(product_id)

    @staticmethod
    def update_product(product_id, data):
        return ProductService.update_product(product_id, data)

    @staticmethod
    def delete_product(product_id):
        return ProductService.delete_product(product_id)

    @staticmethod
    def list_products():
        return ProductService.list_products()
