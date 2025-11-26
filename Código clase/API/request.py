import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

# print(response.status_code)
# print(response.text)

# data = response.json()
# print(data["userId"])

payload = {
    "title": "Nuevo post",
    "body": "Contenido de prueba",
    "userId": 1
}

headers = {
    "Authorization": "Bearer TU_TOKEN_AQUI",
    "Content-Type": "application/json"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload,
    headers=headers
)

print(response.json())
# {'title': 'Nuevo post', 'body': 'Contenido de prueba', 'userId': 1, 'id': 101}
