from utils.db import db

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