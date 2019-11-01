# -*- coding: utf-8 -*-
''' 
 # 7-1
 car = input("Which car do you like?\n")
 print("Let me see if I can find you a " + car)
 
 # 7-2
 people_count = input("How many people?")
 people_count = int(people_count)
 if people_count > 8:
     print("there is no more table")
 else:
     print("welcome")
 
 # 7-3
 num = input("please input a num")
 num = int(num)
 if num%10 == 0:
     print("true")
 else:
     print("false")
 
     # 标志位 flag, 任何条件都转化为设置flag的值
 
    #7-4
while True:
    item = input("what do you want?")
    if item == "quit":
        print("quit system")
        break
    else:
        print("we will serve %s" %item)

# 7-5
flag = True
while True:
    age = input("what is your age?")
    if age == "quit":
        flag = False
    if flag == False:
        break
    age = int(age)
    if age < 3:
        print("free")
    if age >=3 and age <10:
        print("10")
    if age >= 10:
        print("15")
    
'''

#7-8
sandwich_orders = ["aaa","bbb","ccc","ddd","ccc","ccc"]
sandwich_finisheds = []
print("out of ccc")
while "ccc" in sandwich_orders:
    sandwich_orders("ccc")
while sandwich_orders:
# 使用pop来动态遍历
    type = sandwich_orders.pop()
    print("I made your %s sandwich" %type)
    sandwich_finisheds.append(type)
print("\nalready made list:")
for type in sandwich_finisheds:
    print("\t%s sandwich" %type)
# -*- coding: utf-8 -*
names = {}
while True:
    name = input("What is you name?\n")
    place = input("If you could visit one place in the world, where would you go?\n")
#    names = {name:place}
# 字典的添加
    names[name] = place
    ifcon = input("continue? (yes/no)")
    if ifcon == "n":
        break

for name,space in names.items():
    print("%s want to visit %s" %(name,space))



