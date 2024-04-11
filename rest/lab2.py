import requests

res = requests.get("https://randomuser.me/api/")
print(res.headers.get('Content-Type'))
print(res.json())
