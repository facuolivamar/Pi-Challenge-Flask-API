# Import the Schema and fields classes from the marshmallow library
from marshmallow import Schema, fields


# Define a schema for the Character model
class CharacterSchema(Schema):
    id = fields.Int(dump_only=True)

    name = fields.Str(required=True)

    height = fields.Int(required=True)
    mass = fields.Int(required=True)

    hair_color = fields.Str(required=True)
    skin_color = fields.Str(required=True)
    eye_color = fields.Str(required=True)

    birth_year = fields.Int(required=True)
