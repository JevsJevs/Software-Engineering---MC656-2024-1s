from main import app

#check if the list returned is decreasing showing the expected order
def test_get_ratio_correctly():
    instance = app.test_client()
    resp = instance.get("/medals/ratio")
    data = resp.get_json()
    data = data["table"]
    ratioList = list(map(lambda country : country["ratio"], data))
    correctOrder = sorted(ratioList, reverse=True)
    assert correctOrder == ratioList
    assert resp.status_code == 200
