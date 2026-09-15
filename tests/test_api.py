from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"
    assert data["model_loaded"] is True


def test_prediction():

    response = client.post(
        "/predict",
        json={
            "features": [
                5.1,
                3.5,
                1.4,
                0.2
            ]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "prediction" in data


def test_invalid_features():

    response = client.post(
        "/predict",
        json={
            "features": [
                5.1,
                3.5
            ]
        }
    )

    assert response.status_code == 400
