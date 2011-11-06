# -*- coding: utf-8 -*-

import ipfdicttype
import cv

class IPFBlockSizeType(ipfdicttype.IPFDictType):
    """ Block size dict for adaptive threshold
    
    """

    name = "IPFBlockSizeType"
    dictionary = {"3" : 3,
                  "5" : 5,
                  "7" : 7,
                  "9" : 9,
                  "11": 11,}
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["3"]
    