# -*- coding: utf-8 -*
def countword(file,word):
    try:
        with open(file) as f_obj:
            line = f_obj.read()
    except FileNotFoundError:
        print("file not exist")
    else:
        count = line.count(word)
    
    print("the %s comeout  %d times" %(word,count))
    
