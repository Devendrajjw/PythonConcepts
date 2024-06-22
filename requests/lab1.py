import requests

api_url = r'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(api_url)
print(type(response))
print(response)
print(response.status_code)
