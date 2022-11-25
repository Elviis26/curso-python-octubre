import requests


response = requests.get("https://www.breakingbadapi.com/api/characters/" ,
params= {"category" : "Better+Call+Saul"})


requests.post("url", data={"key": "value"})

print(response.status_code)
print(response.json())
walter = response.json()

#print(walter["name"])
#print(walter["occupation"])

print(response.headers)
