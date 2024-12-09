from database import db

from werkzeug.security import check_password_hash

class Employee(db.Model):
    __tablename__ = 'employee'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<Employee {self.username}>'

    def to_dict(self):
        return {
            'id': str(self.id),  
            'username': self.username,
            'password': self.password,
            'role': self.role
        }
