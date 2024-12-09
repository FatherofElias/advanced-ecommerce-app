from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
