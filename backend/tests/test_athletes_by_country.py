from main import app

def test_registered_athlete():
    instance = app.test_client()
    resp = instance.get("/athlete/BRA")
    data = resp.get_json()
    data = data["table"]
    assert resp.status_code == 200
    assert data[0]["id"] == "1351464"
    assert data[0]["nome"] == "ABNER"
    assert data[0]["genero"] == "M"
    assert data[0]["idade"] == "2000-05-27"
    assert data[0]["noc"] == "BRA"


def test_unregistered_country_athlete():
    instance = app.test_client()
    resp = instance.get("/athlete/XXX")
    assert resp.status_code == 404 #country not found

def test_empty_country_medal():
    instance = app.test_client()
    resp = instance.get("/athlete/")
    assert resp.status_code == 404

def test_registered_country_medal():
    instance = app.test_client()
    resp = instance.get("/athlete/HELLOTHISISINVALID")
    assert resp.status_code == 400
