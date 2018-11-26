class a():
                def __init__(self,a,b):
                                self.a=int(a)
                                self.b=int(b)

                def add(self):
                               return self.a+self.b
                                #print("add函数")




class b(a):
                def cut(self):
                                return self.b-self.a
A=b(1,2)
result=A.cut()
print(result)

