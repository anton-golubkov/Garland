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


class Arithmetic(ipfblock.IPFBlock):
    """ Abstract arithmetic block, 
    
        Works with two images, produces one result image of same size  
    
    """
    type = "Arithmetic"
    category = "Arithmetic and logic"
    is_abstract_block = True
    
    def __init__(self):
        super(Arithmetic, self).__init__()
        self.input_ports["input_image_1"] = ioport.IPort(self, IPFImage3cType)
        self.input_ports["input_image_2"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)
        

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
    
    

