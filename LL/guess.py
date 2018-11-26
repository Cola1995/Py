Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num=1
 guess=2
 while guess!=num:
	guess=int(input("请输入你猜的数字："))
	if guess==num:
		print("对了")
	elif guess<num:
		print("小了")
	elif guess>num:
		print("大了")

		
