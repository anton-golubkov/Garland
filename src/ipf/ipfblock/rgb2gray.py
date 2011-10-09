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
    
    def __init__(self):
        super(RGB2Gray, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage1cType)
        
        self.processing_function = ipf.ipfblock.processing.rgb2gray

    def get_preview_image(self):
        return IPFImage3cType.convert(self.output_ports["output_image"]._value)         
        
    
    

