# -*- coding: utf-8 -*
from collections import OrderedDict
from random import randint

dict1 = OrderedDict()
dict2 = {"aaa": 111,"bbb": 222, "ccc": 333}
dict1["aaa"] = 111
dict1["bbb"] = 222
dict1["ccc"] = 333


for k,v in dict1.items():
    print(k,v)
for k,v in dict2.items():
    print(k,v)


class Die():
    def __init__(self):
        self.sides = 6
    def roll_die(self):
        self.sides = randint(1,6)
        return self.sides


sz = Die()

for i in range(1,11):
    print(sz.roll_die())


