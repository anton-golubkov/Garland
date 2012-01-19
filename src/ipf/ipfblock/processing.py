#-------------------------------------------------------------------------------
# Copyright (c) 2011 Anton Golubkov.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Lesser Public License v2.1
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     Anton Golubkov - initial API and implementation
#-------------------------------------------------------------------------------
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
    
    
class process_morphology_1i_1o(object):
    # Decorator class for processing morphology operation 
    # on one 3-channel input image and one output image
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        input_image = args[0]["input_image"]
        element = args[0]["element"]
        if "iterations" in args[0]:
            iterations = args[0]["iterations"]
        else:
            iterations = None
        if not image_empty(input_image):
            output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
            if iterations is not None:
                self.f(input_image,
                       element,
                       iterations,
                       output_image)
            else:
                self.f(input_image,
                       element,
                       output_image)
            output = {"output_image" : output_image}
        else:
            output = {"output_image" : zero_image()}
        return output
    

@process_morphology_1i_1o   
def erosion(input_image,
            element,
            iterations,
            output_image):
    cv.Erode(input_image, output_image, element, iterations)


@process_morphology_1i_1o
def dilate(input_image,
            element,
            iterations,
            output_image):
    cv.Dilate(input_image, output_image, element, iterations)
    

@process_morphology_1i_1o
def opening(input_image,
            element,
            output_image):
    cv.MorphologyEx(input_image, output_image, None, element, cv.CV_MOP_OPEN)
    

@process_morphology_1i_1o
def closing(input_image,
            element,
            output_image):
    cv.MorphologyEx(input_image, output_image, None, element, cv.CV_MOP_CLOSE)
    

@process_morphology_1i_1o
def tophat(input_image,
            element,
            output_image):
    cv.MorphologyEx(input_image, output_image, None, element, cv.CV_MOP_TOPHAT)
    

@process_morphology_1i_1o
def blackhat(input_image,
            element,
            output_image):
    cv.MorphologyEx(input_image, output_image, None, element, cv.CV_MOP_BLACKHAT)
    

def split(input):
    input_image = input["input_image"]
    if not image_empty(input_image):
        output_image_1 = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 1)
        output_image_2 = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 1)
        output_image_3 = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 1)
        cv.Split(input_image, 
                 output_image_1, 
                 output_image_2,
                 output_image_3,
                 None)
        output = {"output_image_1": output_image_1,
                  "output_image_2": output_image_2,
                  "output_image_3": output_image_3,}
    else:
        output = {"output_image_1" : zero_image_1c()}
        output = {"output_image_2" : zero_image_1c()}
        output = {"output_image_3" : zero_image_1c()}
    return output


def merge(input):
    input_image_1 = input["input_image_1"]
    input_image_2 = input["input_image_2"]
    input_image_3 = input["input_image_3"]
    if not image_empty(input_image_1) and \
       not image_empty(input_image_2) and \
       not image_empty(input_image_3):
        # Test same size of input images
        if cv.GetSize(input_image_1) != cv.GetSize(input_image_2) or \
           cv.GetSize(input_image_2) != cv.GetSize(input_image_3):
            output = {"output_image" : zero_image()}
        else:
            # Merge channels
            output_image = cv.CreateImage(cv.GetSize(input_image_1), cv.IPL_DEPTH_8U, 3)
            cv.Merge(input_image_1,
                     input_image_2,
                     input_image_3,
                     None,
                     output_image)
            output = {"output_image" : output_image}
    else:
        output = {"output_image" : zero_image()}
    return output
        


class process_2i_1o(object):
    # Decorator class for processing 2 input images and one output image
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        input_image_1 = args[0]["input_image_1"]
        input_image_2 = args[0]["input_image_2"]
        if not image_empty(input_image_1) and \
           not image_empty(input_image_2):
            # Test same size of input images
            if cv.GetSize(input_image_1) != cv.GetSize(input_image_2):
                output = {"output_image" : zero_image()}
            else:
                output_image = cv.CreateImage(cv.GetSize(input_image_1), cv.IPL_DEPTH_8U, 3)
                self.f(input_image_1,
                       input_image_2,
                       output_image)
                output = {"output_image" : output_image}
        else:
            output = {"output_image" : zero_image()}
        return output


@process_2i_1o
def sum(input_image_1, input_image_2, output_image):
    cv.Add(input_image_1,
           input_image_2,
           output_image)
        
            
@process_2i_1o          
def subtract(input_image_1, input_image_2, output_image):
    cv.Sub(input_image_1,
           input_image_2,
           output_image)


@process_2i_1o          
def multiplication(input_image_1, input_image_2, output_image):
    cv.Mul(input_image_1,
           input_image_2,
           output_image)


@process_2i_1o          
def divide(input_image_1, input_image_2, output_image):
    cv.Div(input_image_1,
           input_image_2,
           output_image)


@process_2i_1o 
def conjunction(input_image_1, input_image_2, output_image):
    cv.And(input_image_1,
           input_image_2,
           output_image)
    

@process_2i_1o 
def disjunction(input_image_1, input_image_2, output_image):
    cv.Or(input_image_1,
          input_image_2,
          output_image)


@process_2i_1o 
def xor(input_image_1, input_image_2, output_image):
    cv.Xor(input_image_1,
           input_image_2,
           output_image)




class process_1i_1o(object):
    # Decorator class for processing one 3-channel input image and one output image
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        input_image = args[0]["input_image"]
        if not image_empty(input_image):
            output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
            self.f(input_image,
                   output_image)
            output = {"output_image" : output_image}
        else:
            output = {"output_image" : zero_image()}
        return output


@process_1i_1o
def invert(input_image, output_image):
    cv.Not(input_image, output_image)
    


class process_threshold(object):
    # Decorator class for processing threshold operation 
    # on one 1-channel input image and one output image
    def __init__(self, f):
        self.f = f

    def __call__(self, *args, **kwargs):
        input_image = args[0]["input_image"]
        threshold_type = args[0]["threshold_type"]
        if "threshold" in args[0]:
            threshold_value = args[0]["threshold"]
        else:
            threshold_value = None
        
        if "adaptive_method" in args[0]:
            adaptive_method = args[0]["adaptive_method"]
            block_size = args[0]["block_size"]
            param = args[0]["param"]
        else:
            adaptive_method = None
        max_value = args[0]["max_value"]
        if not image_empty(input_image):
            output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 1)
            if threshold_value is not None:
                self.f(input_image,
                       threshold_type,
                       threshold_value,
                       max_value,
                       output_image)
            elif adaptive_method is not None:
                self.f(input_image,
                       threshold_type,
                       max_value,
                       adaptive_method,
                       block_size,
                       param,
                       output_image)
            else:
                self.f(input_image,
                       threshold_type,
                       max_value,
                       output_image)
            output = {"output_image" : output_image}
        else:
            output = {"output_image" : zero_image()}
        return output



@process_threshold
def threshold(input_image,
              threshold_type,
              threshold_value,
              max_value,
              output_image):
    cv.Threshold(input_image, 
                 output_image, 
                 threshold_value, 
                 max_value, 
                 threshold_type)


@process_threshold
def threshold_otsu(input_image,
                   threshold_type,
                   max_value,
                   output_image):
    cv.Threshold(input_image, 
                 output_image, 
                 0, 
                 max_value, 
                 threshold_type | cv.CV_THRESH_OTSU)


@process_threshold
def adaptive_threshold(input_image,
                       threshold_type,
                       max_value,
                       adaptive_method,
                       block_size,
                       param,
                       output_image):
    cv.AdaptiveThreshold(input_image,
                         output_image,
                         max_value,
                         adaptive_method,
                         threshold_type,
                         block_size,
                         param)
    



def smooth(input):
    input_image = input["input_image"]
    smoothing_type = input["smoothing_type"]
    aperture_width = input["aperture_width"]
    aperture_height = input["aperture_height"]
    if not image_empty(input_image):
        output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
        cv.Smooth(input_image, 
                  output_image, 
                  smoothing_type,
                  aperture_width,
                  aperture_height)
        output = {"output_image" : output_image}
    else:
        output = {"output_image" : zero_image()}
    return output


def find_chessboard(input):
    input_image = input["input_image"]
    width = input["width"]
    height = input["height"]
    find_type = input["type"] 
    
    if not image_empty(input_image):
        corners = cv.FindChessboardCorners(input_image,
                                           (width, height),
                                           find_type)
        output = {"output_array" : corners[1]}
    else:
        output = {"output_array" : []}
    return output



def sobel(input):
    input_image = input["input_image"]
    xorder = input["xorder"]
    yorder = input["yorder"]
    kernel_size = input["kernel_size"]
    if not image_empty(input_image):
        output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
        temp_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_16S, 3)
        cv.Sobel(input_image, 
                 temp_image, 
                 xorder,
                 yorder,
                 kernel_size)
        cv.ConvertScale(temp_image, output_image)
        output = {"output_image" : output_image}
    else:
        output = {"output_image" : zero_image()}
    return output


def laplace(input):
    input_image = input["input_image"]
    kernel_size = input["kernel_size"]
    if not image_empty(input_image):
        output_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_8U, 3)
        temp_image = cv.CreateImage(cv.GetSize(input_image), cv.IPL_DEPTH_16S, 3)
        cv.Laplace(input_image, 
                   temp_image, 
                   kernel_size)
        cv.ConvertScale(temp_image, output_image)
        output = {"output_image" : output_image}
    else:
        output = {"output_image" : zero_image()}
    return output
