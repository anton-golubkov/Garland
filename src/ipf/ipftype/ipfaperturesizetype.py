# -*- coding: utf-8 -*-

import ipfdicttype
import cv

class IPFApertureSizeType(ipfdicttype.IPFDictType):
    """ Smoothing aperture size type dict
    
    """

    name = "IPFApertureSizeType"
    dictionary = {"1" : 1,
                  "3" : 3,
                  "5" : 5,
                  "7" : 7,
                  "9" : 9,
                  "11" : 11,
                  }
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["1"]
    