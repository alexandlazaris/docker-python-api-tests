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

# check status code
def test_get_store_inventory():
    response = requests.get(constants.BASE_URL + "/store/inventory", headers=headers)
    assert response.status_code == 200

# check status code, response body matches input body, showcasing assertion errors in test output
def test_place_an_order():
    body = {
        "id": 0,
        "petId": 999,
        "quantity": 0,
        "shipDate": "2025-01-16T02:30:32.946Z",
        "status": "placed",
        "complete": True,
    }
    response = requests.post(constants.BASE_URL + "/store/order", headers=headers, json=body)
    data = json.loads(response.content)
    assert data["status"] == 'placed'
    assert data["petId"] == 999
    assert data == body
