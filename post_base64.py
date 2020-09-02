import requests
import base64

url = requests.post('http://xxx.com/')
key = url.headers['flag']
flag = base64.b64decode(key).decode().split(':')[1]
re = {'key':flag}
f = requests.post('http://xxx.com/',data = re)
print(f.text)