from main import app

def test_checkCountryMedal():
    instance = app.test_client()
    # Caso inválido - string NOC deve ter 3 caracteres
    resp = instance.get("/medals/BR")
    data = resp.get_json()
    assert resp.status_code == 400
    assert data["error"] == "Código de país deve ter 3 caracteres."
    resp = instance.get("/medals/BRAS")
    data = resp.get_json()
    assert resp.status_code == 400
    assert data["error"] == "Código de país deve ter 3 caracteres."
    # Caso inválido - País inexistente
    resp = instance.get("/medals/aaa")
    data = resp.get_json()
    assert resp._status_code == 404
    assert data["error"] == "NOC de código 'aaa' não existe."
    # Caso válido
    resp = instance.get("/medals/BRA")
    data = resp.get_json()
    data = data["country"]
    assert resp.status_code == 200
    assert data["nome"] == "Brasil"
    assert data["ouro"] == 29
    assert data["prata"] == 17
    assert data["bronze"] == 9