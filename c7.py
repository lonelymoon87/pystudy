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



