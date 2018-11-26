import urllib.request

response=urllib.request.urlopen('http://124.95.129.86:9000/sso/login')
print(response.read().decode('utf-8'))