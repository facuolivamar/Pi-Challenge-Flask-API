# import db instance and CharacterModel
from models.character import CharacterModel
from utils.db import db


def test_get_character_by_id(client):
    # Create some dummy data
    character1_data = {
        "id": 1,
        "name": "Luke Skywalker",
        "height": 172,
        "mass": 77,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 1998,
    }

    character2_data = {
        "id": 2,
        "name": "Rayo McQueen",
        "height": 230,
        "mass": 100,
        "hair_color": "Golden",
        "skin_color": "Red",
        "eye_color": "Blue",
        "birth_year": 2006
    }

    # Store Characters in db
    character1 = CharacterModel(**character1_data)
    character2 = CharacterModel(**character2_data)
    db.session.add_all([character1, character2])
    db.session.commit()

    # Send GET request to retrieve Luke Skywalker
    response = client.get(f"/character/get/{character1.id}")

    # Check status code
    assert response.status_code == 200

    # Check response data
    data = response.get_json()
    assert all(data[field] == character1_data[field] for field in character1_data)

    # Check all required fields are present in the response
    required_fields = [
        "id",
        "name",
        "height",
        "mass",
        "birth_year",
        "eye_color",
        "hair_color",
        "skin_color"
    ]
    assert all(field in data for field in required_fields)
