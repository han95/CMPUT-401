import requests

response = requests.post('http://ccid-eddieantonio.rhcloud.com/han8')
print(response.status_code)