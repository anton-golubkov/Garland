# -*- coding: utf-8 -*-

import ipftype

class IPFArrayType(ipftype.IPFType):
    """ Base array data type class for use in image processing flow
    
    """

    name = "IPFArrayType"
    this_type = type( [] )
        
    def __init__(self):
        pass
    
        
    @classmethod
    def convert(cls, value):
        """ If value is array, returns this value 
                
        """ 
        if type(value) == type([]):
            return value
        else:
            return []
    
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return []        
    
    @classmethod
    def is_numeric(cls):
        return False
    
    @classmethod
    def is_image(cls):
        return False
    
    @classmethod
    def channel_count(cls):
        return 0
    
    @classmethod
    def is_array(cls):
        return True
    
        