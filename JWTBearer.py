import requests

url = "http://127.0.0.1:8000"

headers = {"Content-Type": "application/json; charset=utf-8"}

response = requests.post(url, headers=headers)

print("Status Code", response.status_code)
print("JSON Response ", response.json())