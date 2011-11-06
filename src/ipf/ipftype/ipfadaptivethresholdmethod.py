# -*- coding: utf-8 -*-

import ipfdicttype
import cv

class IPFAdaptiveThresholdMethod(ipfdicttype.IPFDictType):
    """ Adaptive Threshold Method type dict
    
    """

    name = "IPFAdaptiveThresholdMethod"
    dictionary = {"Mean" : cv.CV_ADAPTIVE_THRESH_MEAN_C,
                  "Gaussian" : cv.CV_ADAPTIVE_THRESH_GAUSSIAN_C,
                  }
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["Mean"]
    