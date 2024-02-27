# Import the Schema and fields classes from the marshmallow library
from marshmallow import Schema, fields


# Define a schema for the Character model based on list retrieval specifications
class CharacterSchemaList(Schema):
    id = fields.Int(required=True)

    name = fields.Str(required=True)

    height = fields.Int(required=True)
    mass = fields.Int(required=True)

    eye_color = fields.Str(required=True)

    birth_year = fields.Int(required=True)


# Define a schema for the Character model based on all of its fields
class CharacterSchema(CharacterSchemaList):
    hair_color = fields.Str(required=True)
    skin_color = fields.Str(required=True)
