from fastapi.testclient import TestClient

from api import __version__
from api.main import app


def test_get_index():
    with TestClient(app) as client:
        response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": f"Welcome to Census Data salary predictor v{__version__}!"
    }


def test_post_high_income():
    data = {
        "age": 45,
        "workclass": "Private",
        "fnlgt": 46781,
        "education": "Masters",
        "education-num": 4,
        "marital-status": "Never-married",
        "occupation": "Prof-specialty",
        "relationship": "Not-in-family",
        "race": "White",
        "sex": "Male",
        "capital-gain": 13084,
        "capital-loss": 0,
        "hours-per-week": 50,
        "native-country": "United-States",
    }
    with TestClient(app) as client:
        response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json() == {"Income": ">50K"}


def test_post_low_income():
    data = {
        "age": 49,
        "workclass": "HS-grad",
        "fnlgt": 160187,
        "education": "9th",
        "education-num": 5,
        "marital-status": "Married-spouse-absent",
        "occupation": "Other-service",
        "relationship": "Not-in-family",
        "race": "Black",
        "sex": "Female",
        "capital-gain": 0,
        "capital-loss": -100,
        "hours-per-week": 5,
        "native-country": "Jamaica",
    }
    with TestClient(app) as client:
        response = client.post("/predict", json=data)
    assert response.status_code == 200
    assert response.json() == {"Income": "<=50K"}


def test_post_fail():
    data = {
        # "age": 49,
        "workclass": "HS-grad",
        "fnlgt": 160187,
        "education": "9th",
        "education-num": 5,
        "marital-status": "Married-spouse-absent",
        "occupation": "Other-service",
        "relationship": "Not-in-family",
        "race": "Black",
        "sex": "Female",
        "capital-gain": 0,
        "capital-loss": -100,
        "hours-per-week": 5,
        "native-country": "Jamaica",
    }
    with TestClient(app) as client:
        response = client.post("/predict", json=data)
    assert response.status_code == 422


def test_post_fail_gt_zero():
    data = {
        "age": -49,
        "workclass": "HS-grad",
        "fnlgt": 160187,
        "education": "9th",
        "education-num": 5,
        "marital-status": "Married-spouse-absent",
        "occupation": "Other-service",
        "relationship": "Not-in-family",
        "race": "Black",
        "sex": "Female",
        "capital-gain": 0,
        "capital-loss": -100,
        "hours-per-week": 5,
        "native-country": "Jamaica",
    }
    with TestClient(app) as client:
        response = client.post("/predict", json=data)
    assert response.json()["detail"][0]["type"] == "value_error.number.not_gt"
    assert response.status_code == 422
