import requests
import json

res = requests.get("https://randomuser.me/api/")
print(res.status_code)
print(res.headers.get('Content-Type'))
print(res.json()) # json available on requests library

dj = res.json()
print(json.dumps(dj)) # converting to python datatypes by json available method in json library
