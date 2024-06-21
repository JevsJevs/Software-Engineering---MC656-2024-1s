from main import app

def test_get_all_medals():
    instance = app.test_client()
    resp = instance.get("/medals")
    data = resp.get_json()
    data = data["table"]
    assert len(data) == 92
    assert resp.status_code == 200
