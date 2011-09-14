# -*- coding: utf-8 -*-

import ipfblock
import ioport
import ipf.ipfblock.processing
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfimage1ctype import IPFImage1cType


class RGB2Gray(ipfblock.IPFBlock):
    """ Convert 3 channel image to 1 channel gray block class
    
    """
    
    def __init__(self):
        super(RGB2Gray, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["gray_image"] = ioport.OPort(self, IPFImage1cType)
        self.type = "RGB2Gray"
        self.processing_function = ipf.ipfblock.processing.rgb2gray

            
        
    
    

