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
import processing
from property import Property
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfstringtype import IPFStringType


class ImageInput(ipfblock.IPFBlock):
    """ Image input block 
    
        Block have 1 output port with type IPFImage3cType
    """
    
    type = "ImageInput"
    category = "Image I/O"
    is_abstract_block = False
    
    def __init__(self):
        super(ImageInput, self).__init__()
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)
        self.processing_function = processing.load_image
        self.properties["file_name"] = Property(IPFStringType)
        
        
    def get_preview_image(self):
        return self.output_ports["output_image"]._value
        
        
        
