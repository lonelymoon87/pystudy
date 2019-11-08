# -*- coding: utf-8 -*
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
# 实参可选，定义形参时用xx=""，并移至末尾





