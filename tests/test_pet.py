import sys
import os
import json

# had to use this as a workaround to pytest throwing an error regarding accessing 'constants'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import src.constants as constants
import requests

headers = {
    "api_key": "special-key",
    "accept": "application/json",
    "Content-Type": "application/json",
}

# check status code, response body matches input body
def test_add_pet():
    body = {
        "id": 123,
        "category": {"id": 0, "name": "string"},
        "name": "doggie",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "available",
    }
    response = requests.post(f"{constants.BASE_URL}/pet", headers=headers, json=body)
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data == body


# check status code, all status param options
def test_find_pet_by_status():
    status_options = ["available", "pending", "sold"]
    for status in status_options:
        params = {"status": status}
        response = requests.get(
            f"{constants.BASE_URL}/pet/findByStatus", headers=headers, params=params
        )
        data = json.loads(response.content)
        assert response.status_code == 200
        assert data[0]["status"] == status
