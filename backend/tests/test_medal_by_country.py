# These tests are of the Unit test type. 
# Their testing method is by defining equivalence input classes 
from main import app

#Equivalent classes:
#search for unregistered country
#search for valid/registered country
#search data empty
#search for invalidData


def test_registered_country_medal():
    instance = app.test_client()
    resp = instance.get("/medals/BRA")
    data = resp.get_json()
    data = data["country"]
    assert resp.status_code == 200
    assert data["nome"] == "Brasil"
    assert data["ouro"] == 29
    assert data["prata"] == 17
    assert data["bronze"] == 9

def test_unregistered_country_medal():
    instance = app.test_client()
    resp = instance.get("/medals/XXX")
    assert resp.status_code == 404 #country not found

def test_empty_country_medal():
    instance = app.test_client()
    resp = instance.get("/medals/")
    assert resp.status_code == 404

def test_registered_country_medal():
    instance = app.test_client()
    resp = instance.get("/medals/HELLOTHISISINVALID")
    assert resp.status_code == 400


