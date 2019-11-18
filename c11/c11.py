# -*- coding: utf-8 -*
def full_city(city,conutry,population=''):
    if population:
        full_city = city + "," + conutry + "-population " + str(population)
    else:
        full_city = city + "," + conutry 
    
    return full_city.title()


