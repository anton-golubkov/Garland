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

class IPFApertureSizeType(ipfdicttype.IPFDictType):
    """ Smoothing aperture size type dict
    
    """

    name = "IPFApertureSizeType"
    dictionary = {"1" : 1,
                  "3" : 3,
                  "5" : 5,
                  "7" : 7,
                  "9" : 9,
                  "11" : 11,
                  }
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["1"]
    
