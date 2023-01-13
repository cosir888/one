import requests

req = requests.get('http://httpbin.org/get')

print(req.text)
