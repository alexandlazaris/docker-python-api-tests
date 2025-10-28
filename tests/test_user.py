import os
import requests

from dotenv import load_dotenv

load_dotenv()

url = os.getenv("BASE_URL")

headers = {
    "api_key": "special-key",
    "accept": "application/json",
    "Content-Type": "application/json",
}

def test_login_as_user():
    USERNAME="username"
    PASSWORD="password"
    response = requests.get(f'{url}/user/login?username={USERNAME}&password={PASSWORD}', headers=headers)
    assert response.status_code == 200
