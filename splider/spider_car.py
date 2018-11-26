import requests
from bs4 import BeautifulSoup
import pymysql

response=requests.get('https://www.autohome.com.cn/news/')
#response.content
response.encoding='gbk'
#print(response.text)

soup=BeautifulSoup(response.text,'html.parser')
# tag=soup.find(id='auto-channel-lazyload-article')
# h3=tag.find(name='h3')
# print(h3)
li_list=soup.find(id='auto-channel-lazyload-article').find_all(name='li')
print(len(li_list))
for li in li_list:
    title=li.find(name='h3')
    if not title:           #如果title为空跳过本次循环
        continue
    des=li.find(name='p')
    #url=li.find(name='a').get('href')
    url=li.find(name='a').attrs['href']
    img=li.find(name='img').attrs['src']
    print(title.text,des.text,url,img)


    db = pymysql.connect(host='localhost', user='root', password='123456', port=3306,db='spiders')  # 创建数据库连接对象
    cursor = db.cursor()  # 获取mysql操作游标
    sql = 'INSERT INTO car_spiders(title,url,img,descption) values(%s,%s,%s,%s)'
    try:
        cursor.execute(sql,(title.text,url,img,des.text))
        db.commit()
    except:
        db.rollback()

    db.close()
