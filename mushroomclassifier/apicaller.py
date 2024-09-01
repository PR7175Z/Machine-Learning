import requests

api = 'http://127.0.0.1:8000/predict'

data = {'features': ['b', 'y', 'w', 't', 'a', 'f', 'c', 'b', 'g', 'e', 'c', 's', 's', 'w','w', 'w','p','w','o', 'p', 'k', 's', 'g']}

response = requests.json(api, json=data)

print(response)