import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update"
# get_response = requests.get(endpoint, params={"abc" : 123}, json={"query" : "Hello World"})
data = {
    "title": "Hello my old friend.",
    "price": 129.99
}
get_response = requests.put(endpoint, json=data)

print(get_response.json())
print(get_response.status_code)