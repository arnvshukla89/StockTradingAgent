# import pytest
# from fastapi.testclient import TestClient
# from src.trading_agent.api.main import app

# client = TestClient(app)

# def test_read_root():
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Welcome to the Stock Trading Agent API"}

# def test_inference_endpoint():
#     response = client.post("/inference", json={"data": [1.0, 2.0, 3.0]})
#     assert response.status_code == 200
#     assert "prediction" in response.json()

# def test_invalid_inference():
#     response = client.post("/inference", json={"data": "invalid_data"})
#     assert response.status_code == 422  # Unprocessable Entity for invalid input

# def test_api_health_check():
#     response = client.get("/health")
#     assert response.status_code == 200
#     assert response.json() == {"status": "healthy"}