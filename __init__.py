
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from flask_jwt_extended import JWTManager
from database import db



db = SQLAlchemy()
cache = Cache()
jwt = JWTManager()

def key_func():
    return request.remote_addr

limiter = Limiter(key_func=key_func)




def create_app(config_name):
    app = Flask(__name__)
    CORS(app)
    jwt = JWTManager(app)
    app.config.from_object(f'config.{config_name}')
    app.config['JWT_SECRET_KEY'] = 'your_secret_key'

    db.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        db.create_all()

    from routes.auth_routes import auth_bp
    from routes.customer_routes import customer_bp
    from routes.customer_account_routes import account_bp
    from routes.product_routes import product_bp
    from routes.order_routes import order_bp

    app.register_blueprint(auth_bp, url_prefix='/api')
    app.register_blueprint(customer_bp, url_prefix='/api')
    app.register_blueprint(account_bp, url_prefix='/api')
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(order_bp, url_prefix='/api')

    return app
