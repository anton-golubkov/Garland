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
import processing
from property import Property
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfstringtype import IPFStringType
from ipf.ipftype.ipfinttype import IPFIntType


class VideoInput(ipfblock.IPFBlock):
    """ Video input block 
    
        Block have 1 output port with type IPFImage3cType
    """
    
    type = "VideoInput"
    category = "Image I/O"
    is_abstract_block = False
    
    def __init__(self):
        super(VideoInput, self).__init__()
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)
        self.processing_function = processing.get_video_image
        self.properties["file_name"] = Property(IPFStringType)
        self.properties["frame"] = Property(IPFIntType, 0)
        self.properties["frame_shift"] = Property(IPFIntType, 0)
        
        
    def get_preview_image(self):
        return self.output_ports["output_image"]._value
        
        
        
