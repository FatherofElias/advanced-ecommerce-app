Advanced E-commerce API
Introduction
The Advanced E-commerce API is a robust and flexible backend solution designed to manage various aspects of an online store, including customer management, product management, order processing, and user authentication using JWT (JSON Web Tokens).

Features
Customer Management: CRUD operations for customer information.

Product Management: CRUD operations for products in the store.

Order Management: Handle orders, including creation and retrieval.

Authentication: Secure user login and JWT-based authorization.

Rate Limiting: Protect endpoints from abuse with request rate limiting.

Caching: Improve performance with caching mechanisms.

Technologies Used
Flask: A lightweight WSGI web application framework.

Flask-RESTful: An extension for Flask that adds support for quickly building REST APIs.

Flask-JWT-Extended: Adds JWT support to Flask.

Flask-SQLAlchemy: Adds SQLAlchemy support to Flask.

Flask-Marshmallow: Adds Marshmallow support for serialization/deserialization.

Flask-Migrate: Handles SQLAlchemy database migrations for Flask applications using Alembic.

Flask-Limiter: Provides rate limiting for Flask applications.

Flask-Caching: Simple caching support for Flask applications.

Pytest: A framework to write simple and scalable test cases.

Installation
Prerequisites
Python 3.8 or higher

pip (Python package installer)

MySQL (or another SQL database)


Setup Instructions
Clone the Repository:

git clone https://github.com/yourusername/advanced_ecommerce_api.git
cd advanced_ecommerce_api


Create and Activate a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:

pip install -r requirements.txt


Set Up the Database:

Make sure you have MySQL running.

Create a database named advanced_e_commerce_db.

Update the config.py file with your database credentials:

class DevelopmentConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'cd8cbabe8c9e4556acb3786fd8389b9b961e8a4f3b34e4748a6a8d4b97c7d4e1')
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:yourpassword@localhost/advanced_e_commerce_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

Run the Application


Endpoints
Authentication
POST /api/auth/login: Authenticate a user and return a JWT.

Customers
POST /customers: Create a new customer.

GET /customers/{id}: Retrieve a customer by ID.

PUT /customers/{id}: Update a customer by ID.

DELETE /customers/{id}: Delete a customer by ID.

Products
POST /products: Create a new product.

GET /products/{id}: Retrieve a product by ID.

PUT /products/{id}: Update a product by ID.

DELETE /products/{id}: Delete a product by ID.

Orders
POST /orders: Create a new order.

GET /orders/{id}: Retrieve an order by ID.









