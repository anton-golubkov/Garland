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
from ipf.ipftype.ipfadaptivethresholdtype import IPFAdaptiveThresholdType
from ipf.ipftype.ipfadaptivethresholdmethod import IPFAdaptiveThresholdMethod
from ipf.ipftype.ipfblocksizetype import IPFBlockSizeType
from ipf.ipftype.ipffloattype import IPFFloatType
from ipf.ipfblock.threshold import Threshold

class AdaptiveThreshold(Threshold):
    """ Adaptive Threshold block
    
    """
    type = "AdaptiveThreshold"
    category = "Filters"
    is_abstract_block = False
    
    def __init__(self):
        super(AdaptiveThreshold, self).__init__()
        self.properties["threshold_type"] = Property(IPFAdaptiveThresholdType)
        self.properties["adaptive_method"] = Property(IPFAdaptiveThresholdMethod)
        self.properties["block_size"] = Property(IPFBlockSizeType)
        self.properties["param"] = Property(IPFFloatType)
        # Adaptive threshold automatically calculate threshold value 
        del self.properties["threshold"]        
        self.processing_function = ipf.ipfblock.processing.adaptive_threshold

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
    
    

