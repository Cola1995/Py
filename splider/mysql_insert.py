import pymysql

# db=pymysql.connect(host='localhost',user='root',password='123456',port=3306)#创建数据库连接对象
# cursor=db.cursor()           #获取mysql操作游标
# cursor.execute('SELECT VERSION()')
# data=cursor.fetchall()  #获取第一条数据
# print(data)
# db.close()

data={'title':1,'url':22}
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')  # 创建数据库连接对象
cursor = db.cursor()  # 获取mysql操作游标
sql='INSERT INTO car_spiders(title,url,img,descption) values("a","b","c","d")'
try:
    cursor.execute(sql)
    print('插入成功')
    db.commit()
except:
    db.rollback()
    print('插入失败')
db.close()


# a={'sex':'nan'}
# data={'id':1,'name':'ma','age':12,'sex':'nv'}
# print(data.values())
