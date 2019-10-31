# -*- coding: utf-8 -*-
# 字典在列表
p1 ={
    "city": "xiamen",
    "fn": "xinxian",
    "age": 18,
    "ln": "zheng",
}
p2 ={
    "city": "xiamen",
    "fn": "qiaoyuan",
    "age": 32,
    "ln": "chen",
}
p3 ={
    "city": "xiamen",
    "fn": "ye",
    "age": 1,
    "ln": "chen",
}

personals = [p1,p2,p3]

for personal in personals[:2]:
    print(personal)


# 6-9 字典嵌套列表
print("-----------")
favority_places = {
    "James": ["tokyo","paris"],
    "Tony": ["taipei","shanghai","beijin"],
    "cindy": ["xiamen"],
}

for name,places in favority_places.items():
    if len(places) == 1:
        print("\n%s's favority place is: \n\t%s" %(name,places[0]))
    else:
        print("\n%s's favority places is:" %name)
        for place in places:
            print("\t"+place)
        
# 6-11 字典嵌套字典
print("\n-----------------\n")
citys = {
    "xiamen": {
        "conuntry": "China",
        "population" : 400,
        "fact": "expensive price",
    },
    "fuzhou": {
        "conuntry": "China",
        "population" : 1000,
        "fact": "dirty mass bad",
    },
    "nanpin": {
        "conuntry": "China",
        "population" : 300,
        "fact": "peace",
    },
}

for city,ats in citys.items():
    print("The city %s's attr:" %city)
    for k,v in ats.items():
        print("\tThe %s is %s" %(k,v))
