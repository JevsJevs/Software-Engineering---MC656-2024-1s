from main import app

def test_checkHome():
    instance = app.test_client()
    resp = instance.get("/")
    data = resp.get_data()
    assert resp.status_code == 200
    assert data == b"<h1>Hello World - Welcome to our project</h1>"

def test_checkCountryMedal():
    instance = app.test_client()
    # Caso inválido - País inexistente
    resp = instance.get("/medals/aaaa")
    data = resp.get_json()
    assert resp._status_code == 404
    assert data["error"] == "NOC de código 'aaaa' não existe."
    # Caso válido
    resp = instance.get("/medals/BRA")
    data = resp.get_json()
    data = data["country"]
    assert resp.status_code == 200
    assert data["nome"] == "Brasil"
    assert data["ouro"] == 29
    assert data["prata"] == 17
    assert data["bronze"] == 9

def test_checkTopMedalTable():
    instance = app.test_client()
    # Caso inválido - Número <= 0
    resp = instance.get("/medals/top/0")
    data = resp.get_json()
    assert resp.status_code == 400
    assert data["error"] == "Número de medalhas deve ser maior que 0"
    # Caso válido
    resp = instance.get("/medals/top/1")
    data = resp.get_json()["table"][0]
    assert resp.status_code == 200
    assert data["codigo"] == "USA"