import json

import requests

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

if __name__ == "__main__":
    response = requests.post(
        "https://udacity-fastapi-ghung.herokuapp.com/predict", data=json.dumps(data)
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response:{response.json()['Income']}")
