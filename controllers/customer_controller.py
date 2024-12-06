from models.customer import db, Customer
from models.customer_account import CustomerAccount
from werkzeug.security import generate_password_hash, check_password_hash

class CustomerController:
    @staticmethod
    def create_customer(data):
        customer = Customer(name=data['name'], email=data['email'], phone=data['phone'])
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
    def create_customer_account(data):
        customer = Customer.query.get(data['customer_id'])
        if customer:
            account = CustomerAccount(
                username=data['username'],
                password=generate_password_hash(data['password']),
                customer=customer
            )
            db.session.add(account)
            db.session.commit()
            return account
        return None

    @staticmethod
    def get_customer_account_by_id(account_id):
        return CustomerAccount.query.get(account_id)

    @staticmethod
    def update_customer_account(account_id, data):
        account = CustomerAccount.query.get(account_id)
        if account:
            account.username = data.get('username', account.username)
            if data.get('password'):
                account.password = generate_password_hash(data['password'])
            db.session.commit()
        return account

    @staticmethod
    def delete_customer_account(account_id):
        account = CustomerAccount.query.get(account_id)
        if account:
            db.session.delete(account)
            db.session.commit()
        return account
