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



class IPFMatchTemplateMethodType(ipfdicttype.IPFDictType):
    """ MatchTemplate method type type dict
    
    """

    name = "IPFMatchTemplateMethodType"
    dictionary = {"CV_TM_SQDIFF" : cv.CV_TM_SQDIFF,
                  "CV_TM_SQDIFF_NORMED" : cv.CV_TM_SQDIFF_NORMED,
                  "CV_TM_CCORR" : cv.CV_TM_CCORR,
                  "CV_TM_CCORR_NORMED" : cv.CV_TM_CCORR_NORMED,
                  "CV_TM_CCOEFF" : cv.CV_TM_CCOEFF,
                  "CV_TM_CCOEFF_NORMED" : cv.CV_TM_CCOEFF_NORMED,
                  }
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return cls.dictionary["CV_TM_SQDIFF"]
    
