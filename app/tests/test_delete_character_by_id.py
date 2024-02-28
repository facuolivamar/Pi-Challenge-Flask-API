from models.character import CharacterModel
from utils.db import db

def test_delete_character(client):
    # Create a store
    character = CharacterModel(
        id= 1,
        name= "Rayo mcqueen",
        height= 230,
        mass= 100,
        hair_color= "Golden",
        skin_color= "Red",
        eye_color= "Blue",
        birth_year= 2006
    )
    db.session.add(character)
    db.session.commit()

    # Send DELETE request
    response = client.delete(f"/character/delete/{character.id}")

    # Check status code
    assert response.status_code == 200
    
    response = client.delete(f"/character/delete/{character.id}")
    data = response.get_json()
    print(data)

    assert data["status"] == "Not Found"
