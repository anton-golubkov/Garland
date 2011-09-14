# -*- coding: utf-8 -*-

import ipftype
import cv

class IPFImage1cType(ipftype.IPFType):
    """ 1 channel image data type class for use in image processing flow
    
    """

    name = "IPFImage1cType"
    this_type = cv.iplimage
        
    def __init__(self):
        pass
    
    @classmethod
    def is_compatible(cls, value):
        """ Return True if type can be converted to this Image
        
        """
        return type(value) == cv.iplimage and value.nChannels == 1
        
    @classmethod
    def convert(cls, value):
        """ Converting not performing, returns passed value
                
        """ 
        return value
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cv.CreateMat(1, 1, cv.CV_8UC1)  
    
    @classmethod
    def is_numeric(cls):
        return False
    
    @classmethod
    def is_image(cls):
        return True
    
    @classmethod
    def channel_count(cls):
        return 1
    
    @classmethod
    def is_array(cls):
        return False