from main import app

def test_checkHome():
    instance = app.test_client()
    resp = instance.get("/")
    data = resp.get_data()
    assert resp.status_code == 200
    assert data == b"<h1>Hello World - Welcome to our project</h1>"

def test_checkCountryMedal():
    instance = app.test_client()
    resp = instance.get("/medals/BRA")
    jsonRoot = resp.get_json()
    data = jsonRoot["country"]
    print(data)
    assert resp.status_code == 200
    assert data["nome"] == "Brasil"
    assert data["ouro"] + data["prata"] + data["bronze"] == 55