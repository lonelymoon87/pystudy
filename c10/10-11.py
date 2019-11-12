# -*- coding: utf-8 -*

import json

def num_store(favnum_file):
    with open(favnum_file,'w') as f_obj:
        favnum = input("please input your favorite number:")
        json.dump(f_obj, favnum)
        

def num_load(favnum_file):
    try:
        with open(favnum_file) as f_obj:
            favnum = json.load(f_obj)
    except  FileNotFoundError:
        return None
    else:
        return favnum




def num_print(favnum_file):
    msg = "I know your favorite number! It's "
    num = num_load(favnum_file)
    if num:
        print(msg+num)
    else:
        num_store(favnum_file)
        num_store(favnum_file)
        print(msg+num)
        
num_print("num.txt")

        

    

 

            



