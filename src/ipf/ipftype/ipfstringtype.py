# -*- coding: utf-8 -*-

import ipftype

class IPFStringType(ipftype.IPFType):
    """ String data type class for use in image processing flow
    
    """

    name = "IPFStringType"
    this_type = type( "" )
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return ""        
    
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
    
        