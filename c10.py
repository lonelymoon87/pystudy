# -*- coding: utf-8 -*-

# read() 读取所有内容到字符串
# 

with open("text.txt") as text:
    print(text.read().strip())
with open("text.txt") as text:
    for line in text:
        print(line.strip())
with open("text.txt") as text:
    line = text.readlines()

print (line)


# -*- coding: utf-8 -*
from countword import countword

# 10-3
# 10-4
'''
while True:
    name = input("Please enter your name:\n")
    if name == 'q':
        break
    print("Hello %s"  %name)
    with open("guest.txt","a") as guest:
        guest.write(name+"\n")


# 10-5

while True:
    reason = input("Please reasons:\n")
    if reason == 'q':
        break
    with open("reason.txt","a") as reasons:
        reasons.write(reason+"\n")
'''

# 10-6
# add 
'''
1. try是要执行的语句，并不是要测试的语句
2. try失败不继续执行，后面的语句需要跟else
'''

'''
while True:
    num1 = input("num1= ")
    try:
        num1 = int(num1)
    except ValueError:
        print("Wrong type,Please input num")
    else:
        num2 = input("num2= ")
        try:
            num2=int(num2)
        except ValueError:
            print("Wrong type,Please input num")
        else:
            print("%d + %d = %d" %(num1,num2,num1+num2))


try:
    with open("dogs.txt") as f_obj:
        dogs = f_obj.readlines()
except FileNotFoundError:
    pass
else:
    for dog in dogs:
        print(dog.strip())


    
try:
    with open("cats.txt") as f_obj:
        dogs = f_obj.readlines()
except FileNotFoundError:
    print("File no found")
else:
    for dog in dogs:
        print(dog.strip())
'''


countword("test1.txt","乔")
