from models import db
from models.order import Order

class OrderService:
    @staticmethod
    def create_order(data):
        order = Order(
            customer_id=data['customer_id'],
            product_id=data['product_id'],
            quantity=data['quantity'],
            total_price=data['total_price']
        )
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def get_order_by_id(order_id):
        return Order.query.get(order_id)

