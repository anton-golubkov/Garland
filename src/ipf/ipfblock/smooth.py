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

import ipf.ipfblock.processing


import ipfblock
import ioport
from property import Property
import ipf.ipfblock.processing
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfsmoothingtype import IPFSmoothingType
from ipf.ipftype.ipfaperturesizetype import IPFApertureSizeType


class Smooth(ipfblock.IPFBlock):
    """ Smooth block  
    
    """
    type = "Smooth"
    category = "Filters"
    is_abstract_block = False
    
    def __init__(self):
        super(Smooth, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)
        self.properties["smoothing_type"] = Property(IPFSmoothingType)
        self.properties["aperture_width"] = Property(IPFApertureSizeType)
        self.properties["aperture_height"] = Property(IPFApertureSizeType)
        self.processing_function = ipf.ipfblock.processing.smooth

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
        

        


