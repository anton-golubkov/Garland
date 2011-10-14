# -*- coding: utf-8 -*-

import ipfblock
import ioport
import ipf.ipfblock.processing
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfimage1ctype import IPFImage1cType


class Merge(ipfblock.IPFBlock):
    """ Merge 3 one-channel images into one RGB 3-channel image
    
    """
    type = "Merge"
    category = "Channel operations"
    is_abstract_block = False
    
    def __init__(self):
        super(Merge, self).__init__()
        self.input_ports["input_image_1"] = ioport.IPort(self, IPFImage1cType)
        self.input_ports["input_image_2"] = ioport.IPort(self, IPFImage1cType)
        self.input_ports["input_image_3"] = ioport.IPort(self, IPFImage1cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)
        self.processing_function = ipf.ipfblock.processing.merge

    def get_preview_image(self):
        return IPFImage3cType.convert(self.output_ports["output_image"]._value)         
        
    
    

