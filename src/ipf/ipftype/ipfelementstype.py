# -*- coding: utf-8 -*-

import ipfdicttype
import cv

class IPFElementsType(ipfdicttype.IPFDictType):
    """ Processing element size dict
    
    """

    name = "IPFElementsType"
    dictionary = {"3x3" : cv.CreateStructuringElementEx(3, 3, 1, 1, cv.CV_SHAPE_RECT),
                  "5x5" : cv.CreateStructuringElementEx(5, 5, 3, 3, cv.CV_SHAPE_RECT),
                  "7x7" : cv.CreateStructuringElementEx(7, 7, 5, 5, cv.CV_SHAPE_RECT),}
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["3x3"]
    