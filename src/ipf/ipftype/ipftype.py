# -*- coding: utf-8 -*-


class IPFType(object):
    """ Base data type class for use in image processing flow
    
    """

    name = "IPFType"
    this_type = type(None)
        
    def __init__(self):
        pass
    
    @classmethod
    def is_compatible(cls, type):
        """ Return True if type can be converted to this IPFType
        
        """
        return cls.is_numeric() == type.is_numeric() and \
               cls.is_array() == type.is_array() and \
               cls.is_image() == type.is_image() and \
               cls.channel_count() == type.channel_count()
    
    @classmethod
    def convert(cls, value):
        """ Convert value to this IPFType 
        
        If converting is not possible function raises exception 
        (ValueError or TypeError)
                
        """ 
        return cls.this_type(value)

            
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return None    
    
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
        return False
    
    
    
        
        
