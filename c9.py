# -*- coding: utf-8 -*

# 9-1
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serverd = 0
    
    def describe_restaurant(self):
        print("\n欢迎光临%s\n我们主营：%s" %(self.restaurant_name,self.cuisine_type))

    def open_restaurant(self):
        print("Restaurant Is Opening")
    
    def set_number_served(self,num):
        self.number_serverd = num
        print("number of people: %d" %self.number_serverd)
    def increment_number_served(self,num):
        self.number_serverd  += num
    







    
myHotel = Restaurant("娴娴和源源的爱心餐馆♥", "沙县小吃")

myHotel.describe_restaurant()
myHotel.open_restaurant()
myHotel.increment_number_served(12)
print(myHotel.number_serverd)
myHotel.increment_number_served(12)
print(myHotel.number_serverd)


# 9-3
class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        print("User Name: %s %s" %(self.first_name.title(), self.last_name.title()))

    
    def greet_user(self):
        print("Hello" + self.last_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0




    
    

user1 = User("qiaoyuan", "chen")

user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()
print(user1.login_attempts)



# 9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    
    
    def print_flavors(self,flavors):
        self.flavors = flavors
        print("\nToday's best sale:")
        for flavor in self.flavors:
            print("\t%s" %flavor)



myice = IceCreamStand("iceshop", "deseate")

myflavor = [111,455,232]

myice.print_flavors(myflavor)





class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privilege()

class Privilege():
    def __init__(self):
        self.privileges = ["can add post","can delete post"]

    def show_privileges(self):
        print("\n you have this privileges:")
        for privilege in self.privileges:
            print("\t%s" %privilege)





admin1 = Admin("qiaoyuan", "chen")

admin1.describe_user()
admin1.greet_user()
admin1.privileges.show_privileges()

# 9-9









