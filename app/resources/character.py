# Import necessary classes from flask views, flask smorest, and sqlalchemy exceptions
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

# Import database instance, Character model and Character schema
from utils.db import db
from models.character import CharacterModel
from schemas.character import CharacterSchema, CharacterSchemaList

# Create a Blueprint for handling character-related operations
blp = Blueprint("Characters", "characters", description="Operations on characters")


# Define endpoints for handling operations on a list of characters
@blp.route("/character/getAll")
class CharacterList(MethodView):
    # Handler for GET request to retrieve all characters
    @blp.response(200, CharacterSchemaList(many=True))
    def get(self):
        return CharacterModel.query.all()

    # Handler for POST request to add a new character
    @blp.arguments(CharacterSchema)
    @blp.response(201, CharacterSchema)
    def post(self, character_data):
        character = CharacterModel(**character_data)

        try:
            db.session.add(character)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the character.")

        return character


# Define endpoints for handling operations on a single character
@blp.route("/character/<int:character_id>")
class Character(MethodView):
    # Handler for GET request to retrieve a single character by ID
    @blp.response(200, CharacterSchema)
    def get(self, character_id):
        # Retrieve the character with the specified ID or abort with a 404
        character = CharacterModel.query.get_or_404(character_id)
        return character

    # Handler for DELETE request to delete a single character by ID
    def delete(self, character_id):
        character = CharacterModel.query.get_or_404(character_id)

        db.session.delete(character)
        db.session.commit()

        return {"message": "Character deleted"}, 200
