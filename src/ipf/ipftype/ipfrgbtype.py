# -*- coding: utf-8 -*-

import ipftype

class IPFRGBType(ipftype.IPFType):
    """ RGB color data type class for use in image processing flow
    
    """

    name = "IPFRGBType"
    this_type = type( [0, 0, 0] )
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return [0, 0, 0]        
    
    @classmethod
    def is_numeric(cls):
        return False
    
    @classmethod
    def is_image(cls):
        return False;
    
    @classmethod
    def channel_count(cls):
        return 0
    
    @classmethod
    def is_array(cls):
        return True
    
        
        
