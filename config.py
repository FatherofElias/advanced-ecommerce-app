import os


class DevelopmentConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'cd8cbabe8c9e4556acb3786fd8389b9b961e8a4f3b34e4748a6a8d4b97c7d4e1')
    SQLALCHEMY_DATABASE_URI = 'postgresql://e_commerce_db_mbe1_user:mQl9Fr7eeKtdztUQxkFcRDtoVNEprSYg@dpg-ctq2pibtq21c739sun5g-a.ohio-postgres.render.com/e_commerce_db_mbe1'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class TestingConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'cd8cbabe8c9e4556acb3786fd8389b9b961e8a4f3b34e4748a6a8d4b97c7d4e1')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True

