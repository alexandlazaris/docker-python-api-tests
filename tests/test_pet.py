import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("BASE_URL")

headers = {
    "api_key": "special-key",
    "accept": "application/json",
    "Content-Type": "application/json",
}


def test_add_pet():
    body = {
        "id": 123,
        "category": {"id": 0, "name": "string"},
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }
    response = requests.post(f"{url}/pet", headers=headers, json=body)
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data == body


def test_get_pet_with_status_available():
    params = {"status": "available"}
    response = requests.get(f"{url}/pet/findByStatus", headers=headers, params=params)
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data[0]["status"] == params["status"]
