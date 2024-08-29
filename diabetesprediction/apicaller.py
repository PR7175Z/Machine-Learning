import requests

# url = 'http://127.0.0.1:4444/predict'
url = 'http://127.0.0.1:8000/predict'

data = {'features': [59, 2,32.1, 101,157, 93.2, 38, 4, 4.8598,87 ]}
response = requests.post(url, json=data)

print(response.json())