

class person:
                name=""
                age=0
                __weight=0
                def __init__(self,n,a,w):
                                self.name=n
                                self.age=a
                                self.weight=w
                def speak(self): 
                                 print("%s说我%s岁%dkg"%(self.name,self.age,self.weight))



class student(person):
                grade=''
                def __init__(self,n,a,w,g):
                                person.__init__(self,n,a,w)
                                self.grade=g
                def speak(self):
                                print("%s说我%s岁%dkg读%d年级"%(self.name,self.age,self.weight,self.grade))
S=student('aaa',10,50,12)
S.speak()
