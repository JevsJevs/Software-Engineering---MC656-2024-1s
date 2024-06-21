from main import app

#Equivalent classes:
#search for valid input
#search data empty
#search for invalidInput

def test_medal_ledger_valid():
    instance = app.test_client()
    testingInput = 10
    resp = instance.get(f"/medals/top/{str(testingInput)}")
    data = resp.get_data()
    assert resp.status_code == 200
    assert len(data) == 10

def test_medal_ledger_empty():
    instance = app.test_client()
    resp = instance.get("/medals/top/")
    assert resp.status_code == 400

def test_medal_ledger_invalid():
    instance = app.test_client()
    resp = instance.get(f"/medals/top/invalidhaha")
    assert resp.status_code == 400

