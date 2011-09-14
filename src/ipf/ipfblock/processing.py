# -*- coding: utf-8 -*-

""" All image processing functions for use in IPFBlock subclasses 

    All functions take dict as parameter {"port_name1" : value1, ...} 
    and returns output ports values in tuple 

"""

import cv

def rgb2gray(input):
    input_image = input["input_image"]
    gray_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 1)
    cv.CvtColor(input_image, gray_image, cv.CV_RGB2GRAY)
    output = {"gray_image":gray_image}
    return output
    
    