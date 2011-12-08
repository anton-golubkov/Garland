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
    
