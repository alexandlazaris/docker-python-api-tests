import sys
import os
# had to use this as a workaround to pytest throwing an error regarding accessing 'constants' 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import src.constants as constants
import requests

ENDPOINT_STORE = constants.BASE_URL + constants.ROUTE_STORE
headers = {
    "api_key": "special-key",
    "accept": "application/json",
    "Content-Type": "application/json",
}


def test_get_store_inventory():
    response = requests.get(ENDPOINT_STORE, headers=headers)
    assert response.status_code == 200


def test_place_an_order_happy():
    body = {
        "id": 0,
        "petId": 0,
        "quantity": 0,
        "shipDate": "2025-01-16T02:30:32.946Z",
        "status": "placed",
        "complete": True,
    }
    response = requests.post(ENDPOINT_STORE, headers=headers, json=body)
    print(response.json())
