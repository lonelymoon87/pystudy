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


