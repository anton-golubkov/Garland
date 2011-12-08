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


class Threshold(ipfblock.IPFBlock):
    """ Threshold block
    
    """
    type = "Threshold"
    category = "Filters"
    is_abstract_block = False
    
    def __init__(self):
        super(Threshold, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage1cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage1cType)    
        self.properties["threshold_type"] = Property(IPFThresholdType)
        self.properties["threshold"] = Property(IPFIntType, 0, 255)
        self.properties["max_value"] = Property(IPFIntType, 0, 255)
        self.processing_function = ipf.ipfblock.processing.threshold

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
    
    

