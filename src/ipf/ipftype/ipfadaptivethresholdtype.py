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
    
