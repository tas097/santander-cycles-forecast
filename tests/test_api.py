from fastapi.testclient import TestClient

from santander_cycles_forecast.api import app

client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_totals_returns_two_stations():
    response = client.get("/totals")
    assert response.status_code == 200
    assert len(response.json()) == 2