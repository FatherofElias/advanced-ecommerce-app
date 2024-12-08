from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Str(required=True)
    stock = fields.Str(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
