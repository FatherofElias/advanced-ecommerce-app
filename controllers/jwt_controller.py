from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.employee import Employee 

class JWTController:

    @staticmethod
    @jwt_required()
    def protected():
        current_employee = get_jwt_identity()
        return jsonify({"message": "Welcome!", "employee": current_employee}), 200

    @staticmethod
    def validate_token(token):
        
        return True

    @staticmethod
    @jwt_required()
    def get_employee_by_token():
        employee_identity = get_jwt_identity()
        return Employee.query.filter_by(id=employee_identity['id']).first()

def setup_jwt_routes(app):
    @app.route('/protected', methods=['GET'])
    @jwt_required()
    def protected_route():
        return JWTController.protected()

    @app.route('/validate-token', methods=['POST'])
    def validate_token_route():
        token = request.json.get('token')
        if JWTController.validate_token(token):
            return jsonify({"message": "Token is valid"}), 200
        else:
            return jsonify({"message": "Token is invalid"}), 400

    @app.route('/employee-from-token', methods=['GET'])
    @jwt_required()
    def employee_from_token_route():
        employee = JWTController.get_employee_by_token()
        if employee:
            return jsonify({"employee": employee.to_dict()}), 200
        else:
            return jsonify({"message": "Employee not found"}), 404
