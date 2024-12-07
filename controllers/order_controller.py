from services.order_service import OrderService

class OrderController:
    @staticmethod
    def create_order(data):
        return OrderService.create_order(data)

    @staticmethod
    def get_order_by_id(order_id):
        return OrderService.get_order_by_id(order_id)
