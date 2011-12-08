#-------------------------------------------------------------------------------
# Copyright (c) 2011 Anton Golubkov.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Lesser Public License v2.1
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     Anton Golubkov - initial API and implementation
#-------------------------------------------------------------------------------
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
    
