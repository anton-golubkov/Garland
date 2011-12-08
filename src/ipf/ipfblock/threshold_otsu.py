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

import ipfblock
import ioport
import ipf.ipfblock.processing
from property import Property
from ipf.ipftype.ipfimage1ctype import IPFImage1cType
from ipf.ipftype.ipfinttype import IPFIntType
from ipf.ipftype.ipfthresholdtype import IPFThresholdType
from ipf.ipfblock.threshold import Threshold

class ThresholdOtsu(Threshold):
    """ Threshold block
    
    """
    type = "ThresholdOtsu"
    category = "Filters"
    is_abstract_block = False
    
    def __init__(self):
        super(ThresholdOtsu, self).__init__()
        # Otsu`s threshold automatically calculate threshold value 
        del self.properties["threshold"]
        self.processing_function = ipf.ipfblock.processing.threshold_otsu

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
    
    

