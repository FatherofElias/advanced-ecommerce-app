
from services.customer_service import CustomerService

class CustomerController:
    @staticmethod
    def create_customer(data):
        return CustomerService.create_customer(data)

    @staticmethod
    def get_customer_by_id(customer_id):
        return CustomerService.get_customer_by_id(customer_id)

    @staticmethod
    def update_customer(customer_id, data):
        return CustomerService.update_customer(customer_id, data)

    @staticmethod
    def delete_customer(customer_id):
        return CustomerService.delete_customer(customer_id)

    @staticmethod
    def list_customers():
        return CustomerService.list_customers()
