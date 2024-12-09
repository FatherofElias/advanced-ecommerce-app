from marshmallow import Schema, fields

class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=False) 
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
