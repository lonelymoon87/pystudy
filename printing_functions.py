# -*- coding: utf-8 -*

def make_car(band,model,**profiles):
    """制作汽车"""
    profiles["band"] = band
    profiles["model"] = model
    return profiles