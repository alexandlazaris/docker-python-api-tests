import requests
import json

url = "https://petstore.swagger.io/v2/swagger.json"
response = requests.get(url)

if response.status_code == 200:
    api_spec = response.json()
    with open("swagger.json", "w") as file:
        json.dump(api_spec, file, indent=2)
else:
    print(f"Failed to fetch API spec, status code: {response.status_code}")
