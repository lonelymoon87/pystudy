# -*- coding: utf-8 -*-
testA="apple"
testB="Apple"
print(testA.lower()==testB.lower() and 1<3)

name1 = ["aaa","bbb","CCC"]
name2 = ["bbb","ccc","ddd"]


for name in name1:
    if name not in name2:
        print(name)

# if elif 只要符合就退出，要多次执行需要多个if

alien_color = "yellow"
if alien_color == "green": 
    print("you got 5 pt!")
elif alien_color == "yellow":
    print("you got 10 pt!")
elif alien_color == "red":
    print("you got 15 pt!")

age = 38

if age < 2:
    print("little baby")
elif age >= 2 and age < 4:
    print("baby")
elif age >= 4 and age < 13:
    print("child")
elif age >= 13 and age < 20:
    print("young")
elif age >= 20 and age < 65:
    print("adult")
elif age >= 65: 
    print("old")

fruits = ["banana", "apple", "orange"]
fruit = "apple"
if fruit in fruits:
    print("You really like %s" %fruit)

# if 列表名 ，如果为空就false
fruits =[]
if fruits:
    print("data")


# 5-8/9
#users = ["aaa","bbb","ccc","ddd","eee","admin"]
users=["aaa", "bbb", "Admin"]
if users:
    for user in users:
        if user.lower()== "admin":
            print("Hello, Admin!")
        else:
            print("Hello %s, thankyou for logging in again" %user)
else:
    print("no users")

# 5-10
users = ["aaa","bbb","ccc","ddd","eee","admin"]
new_users = ["bbb","fff","Admin"]
for user in new_users:
    if user.lower() in users:
        print("%s 已使用" %user)
    else:
        print("%s 可以注册" %user)

# 5-11
for num in range(1,10):
    if num == 1:
        print("1st")
    elif num > 3:
        print("%dth"  %num)
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    



