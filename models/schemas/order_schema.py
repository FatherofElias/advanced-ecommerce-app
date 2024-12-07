from marshmallow import fields
from models import ma

class OrderSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    total_price = fields.Float(required=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)
