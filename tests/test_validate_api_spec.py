import sys
import os
import json
from openapi_spec_validator import validate

# had to use this as a workaround to pytest throwing an error regarding accessing 'constants'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

headers = {
    "api_key": "special-key",
    "accept": "application/json",
    "Content-Type": "application/json",
}

def test_validate_api_spec():
    data = {}
    with open('swagger.json', 'r') as file:
        data = json.load(file)
    validate(data)
    