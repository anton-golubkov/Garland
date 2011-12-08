# -*- coding: utf-8 -*-

import ipfdicttype
import cv

class IPFFindChessboardType(ipfdicttype.IPFDictType):
    """ Find chessboard type dict
    
    """

    name = "IPFFindChessboardType"
    dictionary = {"None" : 0,
                  "Adaptive threshold" : cv.CV_CALIB_CB_ADAPTIVE_THRESH,
                  "Normalize" : cv.CV_CALIB_CB_NORMALIZE_IMAGE,
                  "Filter" : cv.CV_CALIB_CB_FILTER_QUADS,
                  # "Fast check" : cv.CV_CALIB_CB_FAST_CHECK, # Not in that version ?
                  }
        
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["None"]
    