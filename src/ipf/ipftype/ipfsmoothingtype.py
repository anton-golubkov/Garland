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
    
