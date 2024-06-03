from main import app

def test_checkHome():
    instance = app.test_client()
    resp = instance.get("/")
    data = resp.get_data()
    assert resp.status_code == 200
    assert data == b"<h1>Hello World - Welcome to our project</h1>"

def test_checkCountryMedal():
    instance = app.test_client()
    resp = instance.get("/medals/Brasil")
    #TODO: The API must return the data models correctly
    jsonRoot = resp.get_json()
    data = jsonRoot[0]
    print(data)
    assert resp.status_code == 200
    assert data[0] == "Brasil"
    assert sum(data[1:]) == 55