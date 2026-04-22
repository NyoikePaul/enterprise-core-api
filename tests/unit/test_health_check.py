import os
os.environ.setdefault("SECRET_KEY", "test-secret-key-for-unit-tests-only")
 
from fastapi.testclient import TestClient
from src.main import app
 
client = TestClient(app)
 
 
def test_health_returns_200():
    response = client.get("/health")
    assert response.status_code == 200
 
 
def test_health_returns_operational_status():
    response = client.get("/health")
    assert response.json()["status"] == "operational"
 
 
def test_health_returns_version():
    response = client.get("/health")
    assert "version" in response.json()
