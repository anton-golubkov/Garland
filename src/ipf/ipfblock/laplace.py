#-------------------------------------------------------------------------------
# Copyright (c) 2011-2012 Anton Golubkov.
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
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfinttype import IPFIntType
from ipf.ipftype.ipfkernelsizetype import IPFKernelSizeType



class Laplace(ipfblock.IPFBlock):
    """ Laplace operation block 
    
    """
    type = "Laplace"
    category = "Edges"
    is_abstract_block = False
    
    def __init__(self):
        super(Laplace, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)    
        self.properties["kernel_size"] = Property(IPFKernelSizeType)
        self.processing_function = ipf.ipfblock.processing.laplace

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
    