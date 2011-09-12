# -*- coding: utf-8 -*-

import ipftype

class IPFFloatType(ipftype.IPFType):
    """ Float data type class for use in image processing flow
    
    """

    name = "IPFFloatType"
    this_type = type(1.1)
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return 0.0  
    
    @classmethod
    def is_numeric(cls):
        return True
    
    @classmethod
    def is_image(cls):
        return False;
    
    @classmethod
    def channel_count(cls):
        return 0
    
    @classmethod
    def is_array(cls):
        return False
    
        
        
