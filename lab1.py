import requests

response = requests.get('https://github.com/han95/CMPUT-404/raw/master/lab1.py')
print(response.text)