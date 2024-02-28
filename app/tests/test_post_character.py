from models.character import CharacterModel
from utils.db import db


def test_create_character(client):
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

    # Test empty name
    character1_data["name"] = ""
    response = client.post("/character/add", json=character1_data)
    assert response.status_code in [400, 422]

    # Test invalid ID
    character1_data["name"] = "Luke Skywalker"
    character1_data["id"] = 0
    response = client.post("/character/add", json=character1_data)
    assert response.status_code in [400, 422]

    # Test name null
    character1_data["id"] = 1
    character1_data["name"] = None
    response = client.post("/character/add", json=character1_data)
    assert response.status_code in [400, 422]

    # Test invalid mass (string)
    character1_data["name"] = "Luke Skywalker"
    character1_data["mass"] = "mass"
    response = client.post("/character/add", json=character1_data)
    assert response.status_code in [400, 422]

    # Test valid data
    character1_data["mass"] = 77
    response = client.post("/character/add", json=character1_data)
    assert response.status_code in [200, 201]

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
