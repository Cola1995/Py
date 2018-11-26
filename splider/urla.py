import requests
from bs4 import BeautifulSoup

response=requests.get('http://124.95.129.86:9000/manage/index')
#response.content
response.encoding='gbk'
#print(response.text)

soup=BeautifulSoup(response.text,'html.parser')
# tag=soup.find(id='auto-channel-lazyload-article')
# h3=tag.find(name='h3')
# print(h3)

res=requests.get('http://39.106.205.233:8080/GROUP/M00/00/8B/rBHYQFt_wq-AAhPAAAJ9hMtuMNM793.jpg')
filename="zz.jpg"
with open(filename,'wb') as f:
    f.write(res.content)

