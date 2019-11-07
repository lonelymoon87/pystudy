# -*- coding: utf-8 -*

# 10-3
# 10-4
while True:
    name = input("Please enter your name:\n")
    if name == 'q':
        break
    print("Hello %s"  %name)
    with open("guest.txt","a") as guest:
        guest.write(name+"\n")


# 10-5

while True:
    reason = input("Please reasons:\n")
    if reason == 'q':
        break
    with open("reason.txt","a") as reasons:
        reasons.write(reason+"\n")