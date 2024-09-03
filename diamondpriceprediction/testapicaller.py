import requests

api = 'http://127.0.0.1:8000'

data= {'features': [2.03, 4, 6, 3, 62.0, 58.0, 8.06, 8.12, 5.05]}

response = requests.post(api, json=data)

print(response)
