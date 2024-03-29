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
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfimage1ctype import IPFImage1cType


class RGB2Gray(ipfblock.IPFBlock):
    """ Convert 3 channel image to 1 channel gray block class
    
    """
    type = "RGB2Gray"
    category = "Channel operations"
    is_abstract_block = False
    
    def __init__(self):
        super(RGB2Gray, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage1cType)
        
        self.processing_function = ipf.ipfblock.processing.rgb2gray

    def get_preview_image(self):
        return self.output_ports["output_image"]._value          
        
    
    

