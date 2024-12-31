import sys
import os
import unittest
from unittest.mock import patch
from flask_jwt_extended import create_access_token

# Adjust the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from models.customer import Customer
import sqlalchemy.exc

class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('TestingConfig')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            if not Customer.query.filter_by(id=1).first():
                try:
                    admin = Customer(id=1, name='admin', email='admin@example.com', phone='123-456-7890')
                    db.session.add(admin)
                    db.session.commit()
                except sqlalchemy.exc.IntegrityError:
                    db.session.rollback()
            self.token = create_access_token(identity={'id': 1, 'username': 'admin', 'role': 'admin'})

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self.token}'
        }

    @patch('controllers.customer_controller.CustomerController.create_customer')
    def test_create_customer(self, mock_create_customer):
        mock_create_customer.return_value = Customer(id=2, name='John Doe', email='john@example.com', phone='123-456-7890')
        response = self.client.post('/customers', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123-456-7890'
        }, headers=self.get_headers())
        print(f"Request data: {{'name': 'John Doe', 'email': 'john@example.com', 'phone': '123-456-7890'}}")
        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.get_json()}")
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    @patch('controllers.customer_controller.CustomerController.get_customer_by_id')
    def test_get_customer(self, mock_get_customer):
        mock_get_customer.return_value = Customer(id=2, name='John Doe', email='john@example.com', phone='123-456-7890')
        response = self.client.get('/customers/2', headers=self.get_headers())
        print(f"Request data: {{'name': 'John Doe', 'email': 'john@example.com', 'phone': '123-456-7890'}}")
        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.get_json()}")
        self.assertEqual(response.status_code, 200)
        customer_data = response.get_json()
        self.assertEqual(customer_data['name'], 'John Doe')

    @patch('controllers.customer_controller.CustomerController.update_customer')
    def test_update_customer(self, mock_update_customer):
        mock_update_customer.return_value = Customer(id=2, name='John Doe Updated', email='john@example.com', phone='123-456-7890')
        response = self.client.put('/customers/2', json={'name': 'John Doe Updated'}, headers=self.get_headers())
        print(f"Request data: {{'name': 'John Doe Updated', 'email': 'john@example.com', 'phone': '123-456-7890'}}")
        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.get_json()}")
        self.assertEqual(response.status_code, 200)
        customer_data = response.get_json()
        self.assertEqual(customer_data['name'], 'John Doe Updated')

    @patch('controllers.customer_controller.CustomerController.delete_customer')
    def test_delete_customer(self, mock_delete_customer):
        response = self.client.delete('/customers/2', headers=self.get_headers())
        print(f"Request data: {{'name': 'John Doe', 'email': 'john@example.com', 'phone': '123-456-7890'}}")
        print(f"Response status code: {response.status_code}")
        print(f"Response data: {response.get_json()}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'Customer deleted')

if __name__ == '__main__':
    unittest.main()

