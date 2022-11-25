import requests


response = requests.get("https://www.breakingbadapi.com/api/characters/1")

print(response.status_code)
print(response.json())
walter = response.json()[0]

print(walter["name"])
print(walter["occupation"])

print(response.headers)
