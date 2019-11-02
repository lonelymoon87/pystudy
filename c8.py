# -*- coding: utf-8 -*
'''
#8-1
def display_message():
    print("I am learning functions")

display_message()

# 8-2
def favority_book(book):
    print("My favority book is %s" %book)

favority_book(1212)

# 函数参数
# 位置实参、关键字实参、默认值。 默认值实参放在最后。

# 8-3
def make_shirt(size, word="I love python"):
    print("\nThe size is %s with %s on it" %(size,word))

make_shirt(size="XXXL")
make_shirt(size="L")
make_shirt(size="L",word="I love PHP")

# 8-5 
def describe_city(city, country="China"):
    print("%s is in %s" %(city,country))

describe_city("beijin")
describe_city("shanghai")
describe_city("tokyo","Japan")

# 8-6
def city_country(city,country):
    return city+","+country


place1 = city_country("xiamen","China")

print(place1)
# 8-7

def make_album(artist,album,num=""):
    if num:
        return {"name":artist,"albumn":album,"num":num}
    else:
        return {"name":artist,"albumn":album}

player1 = make_album("cqy","xq")
player2 = make_album("jay", "jay")
player2 = make_album("jay", "jay", 12)

print(player1)
print(player2)

# 8-8 

while True:
    artist = input("please enter name\n")
    ablum = input("please enter album\n")
    num = input("please enter num\n")
    if artist == "q" or ablum == "q" or num == "q":
        break
    player = make_album(artist,ablum,num)
    print(player)
# 8-9
magicians = ["aaa","bbb","ccc"]

def show_magi(list):
    for name in list:
        print(name)

def make_great(list):
    list1=[]
    for name in list:
        list1.append("The Great "+name)
    return list1

show_magi(make_great(magicians[:]))
show_magi(make_great(magicians))


print (magicians)

# 函数形参带*表示可以接收多个参数作为元祖
# 函数形参带**表示可以接受多个键值对作为字典

# 8-12
def sandwish(*foods):
    print("\nYou ordered sandwish:")
    for food in foods:
        print("\t %d" %food)
    
sandwish(112,333,444,1111)
sandwish(112)
sandwish(334,333,11233,84)
'''

# 8-13

def user_profile(fname,lname,**profiles):
    profiles["fname"] = fname
    profiles["lname"] = lname
    for profile,value in profiles.items():
        print(profile+": "+str(value))

user_profile("qy","chen",age=18,hight=180,nickname="lonelymoon")

# 8-14
def make_car(band,model,**profiles):
    profiles["band"] = band
    profiles["model"] = model
    return profiles

car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)








        


            

        
    



    




