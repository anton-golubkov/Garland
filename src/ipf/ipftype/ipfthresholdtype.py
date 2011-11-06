# -*- coding: utf-8 -*-

import ipfdicttype
import cv

class IPFThresholdType(ipfdicttype.IPFDictType):
    """ Threshold type dict
    
    """

    name = "IPFThresholdType"
    dictionary = {"Binary" : cv.CV_THRESH_BINARY,
                  "Invert binary" : cv.CV_THRESH_BINARY_INV,
                  "Truncate": cv.CV_THRESH_TRUNC,
                  "To zero": cv.CV_THRESH_TOZERO,
                  "Inverse to zero": cv.CV_THRESH_TOZERO_INV,}
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["Binary"]
    