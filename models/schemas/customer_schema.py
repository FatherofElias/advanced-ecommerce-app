from marshmallow import fields
from models import ma

class CustomerSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True)
    phone = fields.Str(required=True)

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
