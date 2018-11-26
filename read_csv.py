import csv

my_file='userinfo.csv'
data=csv.reader(open(my_file,'r'))
for s in data:
    print(s[3])