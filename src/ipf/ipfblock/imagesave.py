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

class ImageSave(ipfblock.IPFBlock):
    """ Image save block 
    
        Block have 1 input port with type IPFImage3cType 
    """
    
    type = "ImageSave"
    category = "Image I/O"
    is_abstract_block = False
    
    def __init__(self):
        super(ImageSave, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)    
        self.processing_function = processing.save_image
        self.properties["file_name"] = Property(IPFStringType)
        
    def get_preview_image(self):
        return self.input_ports["input_image"]._value  
