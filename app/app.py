# Import necessary classes from flask, flask_smorest(REST API), and flask_migrate
from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate

# Import database instance and Character blueprint(endpoints)
from utils.db import db
from resources.character import blp as CharacterBlueprint


# Function to create the Flask application
def create_app(db_url=None):
    app = Flask(__name__)

    # Configure Flask application settings
    app.config["API_TITLE"] = "Characters REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config[
        "OPENAPI_SWAGGER_UI_URL"
    ] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True

    # Initialize and configure database and migration
    db.init_app(app)
    migrate = Migrate(app, db)

    # Initialize API
    api = Api(app)

    # Create database tables
    with app.app_context():
        db.create_all()

    # Register Character blueprint in the API
    api.register_blueprint(CharacterBlueprint)

    return app
