# -*- coding: utf-8 -*-

import ipfblock
import ioport
import ipf.ipfblock.processing
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfimage1ctype import IPFImage1cType


class Sum(ipfblock.IPFBlock):
    """ Summarize two images 
    
    """
    type = "Sum"
    category = "Arithmetic and logic"
    is_abstract_block = False
    
    def __init__(self):
        super(Sum, self).__init__()
        self.input_ports["input_image_1"] = ioport.IPort(self, IPFImage3cType)
        self.input_ports["input_image_2"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)
        self.processing_function = ipf.ipfblock.processing.sum

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
    
    

