import requests


url = 'http://127.0.0.1:8000/form/process'
data = {
	'name': 'Ruslan',
	'phone': '+79998303814',
	'email': 'recursion198@gmail.com',
	'courseid': 'product109195238'
}

response = requests.post(url, data=data)

print(response.json())
