from main import app
#Equivalent classes:
#search for valid/registered category
#search data empty

def test_valid_category():
    instance = app.test_client()
    resp = instance.get(f"/medals/category/athletics")
    data = resp.get_json()
    data = data["table"]
    assert resp.status_code == 200
    assert len(data) > 0

def test_empty_category():
    instance = app.test_client()
    resp = instance.get("/medals/category/")
    assert resp.status_code == 404