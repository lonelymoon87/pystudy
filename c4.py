# -*- coding: utf-8 -*-
'''
pizzas = ["beef","pork","chess","seafood"]
for pizza in pizzas:
    print("I like %s pizza" %pizza)
print("I really love pizza")


# 列表解析
# 列表名 = [列表值 列表表达式(for x in xxx)]
for num in range(1,21):
    print(num)
lnum = [num for num in range(1,1000001)]
print(max(lnum))
print(min(lnum))

'''

### 列表解析 包含for和if

div = [num for num in range(3,31) if num%3 == 0]
for i in div:
    print(i)

lit = [x**3 for x in range(1,11)]
for i in lit:
    print(i)

### 列表切片
## 开始n个
print(lit[:3])
## 最后n个
print(lit[-3:])
## 可以只遍历切片
for i in lit[-3:]:
    print(i)

## 复制列表,不用切片
kee = lit
print(kee)
lit.append(11222)
print(kee)
## 复制列表,用切片,才是不同列表
kee = lit[:]
print(kee)
lit.append(11222)
print(lit)
print(kee)

print(len(kee)/2)

# 元祖 不可改变

dim = (112,332,454)

print(dim[2])
dim = (213,122,334)
for i in dim:
    print(i)
    