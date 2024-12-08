from database import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.String, nullable=False)
    stock = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'
