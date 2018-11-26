
import os
 
#定义文件目录
result_dir = r"C:\Users\Administrator\Desktop\Py\test_report"
 
lists = os.listdir(result_dir) #获取该目录下的所有文件、文件夹，保存为列表
 
#对目录下的文件按创建的时间进行排序
lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
#lists[-1]取到的是最新生成的文件或文件夹
print(('最新的文件是：' + lists[-1])) 
