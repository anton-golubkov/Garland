# -*- coding: utf-8 -*-

import ipfdicttype
import cv

class IPFElementsType(ipfdicttype.IPFDictType):
    """ Processing element size dict
    
    """

    name = "IPFElementsType"
    dictionary = {"3x3" : cv.CreateMat(3, 3, cv.CV_8S),
                  "5x5" : cv.CreateMat(5, 5, cv.CV_8S),
                  "7x7" : cv.CreateMat(7, 7, cv.CV_8S),}
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["3x3"]
    