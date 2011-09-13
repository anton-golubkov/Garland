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
        return False;