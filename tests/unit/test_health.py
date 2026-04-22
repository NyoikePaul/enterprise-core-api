import os
os.environ.setdefault("SECRET_KEY", "test-secret-key-for-unit-tests-only")
 
from fastapi.testclient import TestClient
from src.main import app
 
client = TestClient(app)
 
 
def test_health_check_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "operational"
    assert "version" in body
