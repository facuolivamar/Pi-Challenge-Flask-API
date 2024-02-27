from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from utils.db import db
from models.character import CharacterModel
from schemas.character import CharacterSchema

blp = Blueprint("Characters", "characters", description="Operations on characters")

@blp.route("/character")
class CharacterList(MethodView):
    @blp.response(200, CharacterSchema(many=True))
    def get(self):
        return CharacterModel.query.all()

    
