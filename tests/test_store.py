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

def test_get_store_inventory():
    response = requests.get(f'{url}/store/inventory', headers=headers)
    assert response.status_code == 200

def test_place_an_order():
    body = {
        "id": 0,
        "petId": 999,
        "quantity": 0,
        "shipDate": "2025-01-16T02:30:32.946Z",
        "status": "placed",
        "complete": True,
    }
    response = requests.post(f'{url}/store/order', headers=headers, json=body)
    data = json.loads(response.content)
    assert data["status"] == 'placed'
    assert data["petId"] == 999
    assert data["complete"] == True
    assert isinstance(data["id"], int)