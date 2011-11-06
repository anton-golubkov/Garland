# -*- coding: utf-8 -*-

import ipfdicttype
import cv

class IPFAdaptiveThresholdType(ipfdicttype.IPFDictType):
    """ Adaptive Threshold type dict
    
    """

    name = "IPFAdaptiveThresholdType"
    dictionary = {"Binary" : cv.CV_THRESH_BINARY,
                  "Invert binary" : cv.CV_THRESH_BINARY_INV,
                  }
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["Binary"]
    