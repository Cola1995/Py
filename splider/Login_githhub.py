import requests
from bs4 import BeautifulSoup


response=requests.get('https://github.com/login')
response.encoding='gbk'
soup=BeautifulSoup(response.text,'html.parser')
token=soup.find(name='input',attrs={'name':'authenticity_token'}).get('value')  #获取token
#print(token)
cook_dict=response.cookies.get_dict()
'''
utf8: ✓
authenticity_token: Cz1Bx5ZjCoqjZKBHfMqmN1Xss4LeEL6c61uPQ6ZdqnaU7vbP73AxXIPg97lCQ//GyJ5BSFNf+RmUK0LQBt7svw==
login: ss
password: ss
'''
r2=requests.post('https://github.com/session',
                 data={'utf8': '✓',
                       'authenticity_token': token,
                       'login': '317828332@qq.com',
                       'password': 'alex3714',
                       'commit': 'Sign in'
},
                 cookies=cook_dict

)
#print(r2.text)
r2_cookies_dict=r2.cookies.get_dict()
cookies_dict={}            #合并两次请求的cookies
cookies_dict.update(cook_dict)
cookies_dict.update(r2_cookies_dict)
r3=requests.get('https://github.com/settings/emails',cookies=cookies_dict)
print(r3.text)
