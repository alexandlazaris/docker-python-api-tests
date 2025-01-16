import sys
import os

# had to use this as a workaround to pytest throwing an error regarding accessing 'constants'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import src.constants as constants
import requests

headers = {
    "api_key": "special-key",
    "accept": "application/json",
    "Content-Type": "application/json",
}

def test_login_as_user():
    response = requests.get(constants.BASE_URL + "/user/login?username=username&password=password", headers=headers)
    assert response.status_code == 200
