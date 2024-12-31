from services.customer_service import CustomerService

class CustomerController:
    @staticmethod
    def create_customer(data):
        try:
            print(f"Data in create_customer: {data}")
            customer = CustomerService.create_customer(data)
            print(f"Customer created: {customer.to_dict()}")
            return customer
        except Exception as e:
            print(f"Error in create_customer: {e}")
            raise e

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
