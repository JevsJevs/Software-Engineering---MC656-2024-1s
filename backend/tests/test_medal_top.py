from main import app

#Equivalent classes:
#search for valid input
#search data empty
#search for invalidInput

def test_medal_ledger_valid():
    instance = app.test_client()
    resp = instance.get("/medals/top/10")
    data = resp.get_json()
    data = data["table"]
    assert resp.status_code == 200
    assert len(data) == 10

def test_medal_ledger_empty():
    instance = app.test_client()
    resp = instance.get("/medals/top/")
    assert resp.status_code == 404

def test_medal_ledger_invalid():
    instance = app.test_client()
    resp = instance.get(f"/medals/top/invalidhaha")
    assert resp.status_code == 404

