import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'cd8cbabe8c9e4556acb3786fd8389b9b961e8a4f3b34e4748a6a8d4b97c7d4e1')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+pymysql://root:ELias928@localhost/advanced_e_commerce_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = 'simple'
    RATELIMIT_DEFAULT = '100 per day'
    JWT_SECRET_KEY = 'your_jwt_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
