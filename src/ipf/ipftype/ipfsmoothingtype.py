# -*- coding: utf-8 -*-

import ipfdicttype
import cv

class IPFSmoothingType(ipfdicttype.IPFDictType):
    """ Smoothing type dict
    
    """

    name = "IPFSmoothingType"
    dictionary = {"Blur" : cv.CV_BLUR,
                  "Gaussian" : cv.CV_GAUSSIAN,
                  "Median" : cv.CV_MEDIAN,
                  # "Bilateral" : cv.CV_BILATERAL, # TODO: Need understand algorithm and use param3 and param4
                  }
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["Blur"]
    