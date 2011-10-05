# -*- coding: utf-8 -*-

import ipftype
import cv

class IPFImage3cType(ipftype.IPFType):
    """ 3 channel image data type class for use in image processing flow
    
    """

    name = "IPFImage3cType"
    this_type = cv.iplimage
        
    def __init__(self):
        pass
    
    
    @classmethod
    def is_compatible(cls, type):
        """ Return True if type can be converted to this Image
        
            Converting from 1 channel image to 3 channel is accepted
        """
        return type.this_type == cv.iplimage and \
               (type.channel_count() == 3 or type.channel_count() == 1) 
            
    @classmethod
    def convert(cls, value):
        """ If necessary convert 1 channel image to 3 channel
        
        """ 
        if( value.nChannels == 1):
            image3c = cv.CreateImage(cv.GetSize(value), cv.IPL_DEPTH_8U, 3)
            cv.Merge(value, value, value, None, image3c)
            return image3c
        else:
            return value
    
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cv.CreateMat(1, 1, cv.CV_8UC3)  
    
    @classmethod
    def is_numeric(cls):
        return False
    
    @classmethod
    def is_image(cls):
        return True
    
    @classmethod
    def channel_count(cls):
        return 3
    
    @classmethod
    def is_array(cls):
        return False