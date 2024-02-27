# Import database instance and validates from sqlalchemy
from utils.db import db
from sqlalchemy.orm import validates

# Define the Character table/model
class CharacterModel(db.Model):

    __tablename__ = "Characters"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(80), unique=False, nullable=False)

    height = db.Column(db.Integer, unique=False, nullable=False)
    mass = db.Column(db.Integer, unique=False, nullable=False)

    hair_color = db.Column(db.String(80), unique=False, nullable=False)
    skin_color = db.Column(db.String(80), unique=False, nullable=False)
    eye_color = db.Column(db.String(80), unique=False, nullable=False)

    birth_year = db.Column(db.Integer, unique=False, nullable=False)

    @validates('id', 'height', 'mass')
    def validate_positive(self, key, value):
        if value <= 0:
            raise ValueError(f"{key.capitalize()} must be greater than 0.")
        return value

    @validates('name', 'hair_color', 'skin_color', 'eye_color')
    def validate_non_empty(self, key, value):
        if not value.strip():
            raise ValueError(f"{key.capitalize()} cannot be empty.")
        return value