# -*- coding: utf-8 -*-

""" All image processing functions for use in IPFBlock subclasses 

    All functions take input ports values as parameters and returns output port 
    values in tuple 

"""

import cv

def rgb2gray(input_image):
    gray_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 1)
    cv.CvtColor(input_image, gray_image, cv.CV_RGB2GRAY)
    return (gray_image)
    
    