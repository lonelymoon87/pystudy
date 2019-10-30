# -*- coding: utf-8 -*-
location = ["nz","tokyo","easte","wa","sing"]
print(location)
#使用sorted(list),不改变原列表
print(sorted(location))
print(location)
print(sorted(location,reverse=True))
print(location)

location.reverse()
print(location)
location.sort()
print(location)
location.sort(reverse=True)
print(location)

print ("there are %d place want to go to" %(len(location)))