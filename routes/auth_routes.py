
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from utils.jwt_utils import generate_token
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify
from models.employee import Employee
from models.schemas.employee_schema import EmployeeSchema
from werkzeug.security import generate_password_hash 
from utils.jwt_utils import generate_token
from flask_jwt_extended import jwt_required
from __init__ import db

auth_bp = Blueprint('auth_bp', __name__)

employee_schema = EmployeeSchema()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    employee = Employee.query.filter_by(username=data['username']).first()
    if employee and employee.check_password(data['password']):
        token = generate_token(employee)
        return jsonify({'token': token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = employee_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    username = data['username']
    password = data['password']
    role = data.get('role', 'user') 

    if Employee.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 409

    hashed_password = generate_password_hash(password)
    new_employee = Employee(username=username, password=hashed_password, role=role)

    db.session.add(new_employee)
    db.session.commit()

    token = generate_token(new_employee)
    return jsonify({'token': token, 'message': 'Account created successfully'}), 201



@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    try:
        current_user_id = get_jwt_identity()
        print(f"Current user ID: {current_user_id}")
        return jsonify({"message": f"Access granted for user {current_user_id}"}), 200
    except Exception as e:
        print(f"Error in protected route: {e}")
        return jsonify({"message": str(e)}), 500
