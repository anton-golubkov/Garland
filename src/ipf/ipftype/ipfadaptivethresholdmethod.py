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
    
