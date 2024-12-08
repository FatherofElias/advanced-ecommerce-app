from database import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    account_id = db.Column(db.Integer, db.ForeignKey('customer_account.id'))
    account = db.relationship('CustomerAccount', back_populates='customers')

    def __repr__(self):
        return f'<Customer {self.name}>'
