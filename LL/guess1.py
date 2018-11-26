num=1
guess=2
while guess!=num:
                guess=int(input("请输入一个数字"))
                if guess==num:
                                
                                print("对了")
                                #break
                elif guess>num:
                                print("大了")
                elif guess<num:
                                print("小了")
