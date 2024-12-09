from database import db
from models.customer import Customer

class CustomerService:
    @staticmethod
    def create_customer(data):
        customer = Customer(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone') 
        )
        db.session.add(customer)
        db.session.commit()
        return customer

    @staticmethod
    def get_customer_by_id(customer_id):
        return Customer.query.get(customer_id)

    @staticmethod
    def update_customer(customer_id, data):
        customer = Customer.query.get(customer_id)
        if customer:
            customer.name = data.get('name', customer.name)
            customer.email = data.get('email', customer.email)
            customer.phone = data.get('phone', customer.phone)
            db.session.commit()
        return customer

    @staticmethod
    def delete_customer(customer_id):
        customer = Customer.query.get(customer_id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
        return customer

    @staticmethod
    def list_customers():
        return Customer.query.all()
