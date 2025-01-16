import sys
import os
import json
# had to use this as a workaround to pytest throwing an error regarding accessing 'constants'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import src.constants as constants
import requests

ENDPOINT_PET = constants.BASE_URL + constants.ROUTE_PET
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
    response = requests.post(ENDPOINT_PET, headers=headers, json=body)
    assert response.status_code == 200

def test_find_pet_by_status_available():
    response = requests.get(ENDPOINT_PET + "/findByStatus?status=available", headers=headers)
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data[0]["status"] == 'available'

