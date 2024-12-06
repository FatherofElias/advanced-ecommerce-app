from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_limiter import Limiter
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
cache = Cache()
limiter = Limiter()
jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    db.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    jwt.init_app(app)

    from routes.customer_routes import customer_bp
    from routes.customer_account_routes import account_bp
    from routes.product_routes import product_bp
    from routes.order_routes import order_bp

    app.register_blueprint(customer_bp, url_prefix='/api')
    app.register_blueprint(account_bp, url_prefix='/api')
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(order_bp, url_prefix='/api')

    return app
