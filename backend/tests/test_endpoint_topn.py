from main import app

def test_checkTopMedalTable():
    instance = app.test_client()
    # Caso inválido - Número <= 0
    resp = instance.get("/medals/top/0")
    data = resp.get_json()
    assert resp.status_code == 400
    assert data["error"] == "Número de medalhas deve ser maior que 0"
    # Caso válido
    resp = instance.get("/medals/top/1")
    data = resp.get_json()["table"]
    assert resp.status_code == 200
    assert len(data) == 1