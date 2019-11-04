# -*- coding: utf-8 -*

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    '''电动汽车'''
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery():
    """模拟电池"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size
    
    def get_range(self):
        if self.battery_size < 80:
            range = 240
        else:
            range = 270
        print("range is " + str(range))
    
    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85