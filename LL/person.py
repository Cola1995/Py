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
#p=person("ma",23,60)
#p.speak()
 
