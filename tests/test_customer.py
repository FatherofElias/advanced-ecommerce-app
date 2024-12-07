import unittest
from __init__ import create_app, db
from models.customer import Customer

class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('development')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_customer(self):
        response = self.client.post('/api/customers', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123-456-7890'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_customer(self):
    
        response = self.client.post('/api/customers', json={
            'name': 'John Doe',
            'email': 'john@example.com',
            'phone': '123-456-7890'
        })
        self.assertEqual(response.status_code, 201)
        customer_id = response.get_json()['id']

        
        response = self.client.get(f'/api/customers/{customer_id}')
        self.assertEqual(response.status_code, 200)
        
        customer_data = response.get_json()
        self.assertEqual(customer_data['name'], 'John Doe')
        self.assertEqual(customer_data['email'], 'john@example.com')
        self.assertEqual(customer_data['phone'], '123-456-7890')

if __name__ == '__main__':
    unittest.main()
