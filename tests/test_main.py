from fastapi.testclient import TestClient
from main import app
client= TestClient(app)

def test_calculate_stats():
    response=client.post("/calculate/",json={"numbers":[10,20,30,40,50]})
    assert response.status_code==200
    data=response.json()
    assert data["mean"]==30.0
    assert data["variance"]==200.0
    assert round(data["standard_deviation"],5)==14.14214

def test_empty_list():
    response=client.post("/calculate/",json={"numbers":[]})
    assert response.status_code==400