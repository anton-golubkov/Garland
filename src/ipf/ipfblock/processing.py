# -*- coding: utf-8 -*-

""" All image processing functions for use in IPFBlock subclasses 

    All functions take dict as parameter {"port_name1" : value1, ...} 
    and returns output ports values in tuple 

"""

import cv


def zero_image():
    return cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)

    
def zero_image_1c():
    return cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 1)


def image_empty(image):
    return cv.GetSize(image) == (0, 0)


def rgb2gray(input):
    input_image = input["input_image"]
    if not image_empty(input_image):
        gray_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 1)
        cv.CvtColor(input_image, gray_image, cv.CV_RGB2GRAY)
        output = {"output_image" : gray_image}
    else:
        output = {"output_image" : zero_image_1c()}
    return output

def load_image(input):
    file_name = input["file_name"]
    try:
        output_image = cv.LoadImage(file_name)
    except IOError:
        # file not found, returns zero image
        output = {"output_image": zero_image()}
    else: 
        output = {"output_image" : output_image}
    return output

def save_image(input):
    file_name = input["file_name"]
    saving_image = input["input_image"]
    if len(file_name) > 0:
        cv.SaveImage(file_name, saving_image)
    return {}
    
    
def erosion(input):
    input_image = input["input_image"]
    element = input["element"]
    iterations = input["iterations"]
    if not image_empty(input_image):
        output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
        cv.Erode(input_image, output_image, element, iterations)
        output = {"output_image": output_image}
    else:
        output = {"output_image" : zero_image()}
    return output


def dilate(input):
    input_image = input["input_image"]
    element = input["element"]
    iterations = input["iterations"]
    if not image_empty(input_image):
        output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
        cv.Dilate(input_image, output_image, element, iterations)
        output = {"output_image": output_image}
    else:
        output = {"output_image" : zero_image()}
    return output


def opening(input):
    input_image = input["input_image"]
    element = input["element"]
    if not image_empty(input_image):
        output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
        cv.MorphologyEx(input_image, output_image, None, element, cv.CV_MOP_OPEN)
        output = {"output_image": output_image}
    else:
        output = {"output_image" : zero_image()}
    return output


def closing(input):
    input_image = input["input_image"]
    element = input["element"]
    if not image_empty(input_image):
        output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
        cv.MorphologyEx(input_image, output_image, None, element, cv.CV_MOP_CLOSE)
        output = {"output_image": output_image}
    else:
        output = {"output_image" : zero_image()}
    return output


def tophat(input):
    input_image = input["input_image"]
    element = input["element"]
    if not image_empty(input_image):
        output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
        cv.MorphologyEx(input_image, output_image, None, element, cv.CV_MOP_TOPHAT)
        output = {"output_image": output_image}
    else:
        output = {"output_image" : zero_image()}
    return output
