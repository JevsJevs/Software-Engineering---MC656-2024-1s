from main import app

def test_get_all_categories():
    instance = app.test_client()
    resp = instance.get("/categories")
    data = resp.get_json()
    data = data["table"]
    assert len(data) == 46
    assert resp.status_code == 200