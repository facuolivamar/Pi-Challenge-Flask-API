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


# Define endpoint for retrieving a list of characters
@blp.route("/character/getAll")
class CharacterList(MethodView):

    # Handler for GET request to retrieve all characters
    @blp.response(200, CharacterSchemaList(many=True))
    def get(self):
        return CharacterModel.query.all()


# Define endpoint for inserting a new character
@blp.route("/character/add")
class CharacterPost(MethodView):

    # Handler for POST request to add a new character
    @blp.arguments(CharacterSchema)
    @blp.response(201, CharacterSchema)
    def post(self, character_data):
        character = CharacterModel(**character_data)

        try:
            db.session.add(character)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(400, message=e._message())

        return character


# Define endpoint for retrieving a single character based on its id
@blp.route("/character/get/<int:character_id>")
class CharacterGet(MethodView):

    # Handler for GET request to retrieve a single character by ID
    @blp.response(200, CharacterSchema)
    def get(self, character_id):
        character = CharacterModel.query.get_or_404(character_id)

        return character


# Define endpoint for deleting a character based on its id
@blp.route("/character/delete/<int:character_id>")
class CharacterDelete(MethodView):

    # Handler for DELETE request to delete a character by ID
    def delete(self, character_id):
        character = CharacterModel.query.get_or_404(character_id)

        db.session.delete(character)
        db.session.commit()

        return {"message": "Character deleted"}, 200
