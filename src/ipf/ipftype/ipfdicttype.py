# -*- coding: utf-8 -*-

import ipftype
from ipf.keyfromvalue import dict_key_from_value

class IPFDictType(ipftype.IPFType):
    """ Base dictionary type
    
        Class used as parent for all value list types
    """

    name = "IPFDictType"
    this_type = type(dict())
    dictionary = dict()
        
    def __init__(self):
        pass
    
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return None
    
    @classmethod
    def convert(cls, key):
        """ Returns dict value for given key 
        
                
        """ 
        return cls.dictionary[key]
    
    @classmethod
    def get_keys(cls):
        return cls.dictionary.keys()
    
    
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
    
    
    @classmethod
    def get_value_representation(cls, value):
        """ Return displaying data for value """
        return dict_key_from_value(cls.dictionary, value)
    
    
    @classmethod
    def get_value_list(cls):
        """ Return list of all possible values """
        return cls.dictionary.values()
    
        
        
