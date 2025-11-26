import requests

url = "https://picsum.photos/200/300?grayscale"

response = requests.get(url)

# print(response.content)

with open("imagen2.png", "wb") as file:
    file.write(response.content)
