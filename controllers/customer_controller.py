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
    def create_customer_account(data):
        return CustomerService.create_customer_account(data)

    @staticmethod
    def get_customer_account_by_id(account_id):
        return CustomerService.get_customer_account_by_id(account_id)

    @staticmethod
    def update_customer_account(account_id, data):
        return CustomerService.update_customer_account(account_id, data)

    @staticmethod
    def delete_customer_account(account_id):
        return CustomerService.delete_customer_account(account_id)
