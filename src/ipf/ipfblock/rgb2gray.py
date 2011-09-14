# -*- coding: utf-8 -*-

import ipfblock
import ioport
from ipftype.ipfimage3ctype import IPFImage3cType
from ipftype.ipfimage1ctype import IPFImage1cType
import processing

class RGB2Gray(ipfblock.IPFBlock):
    """ Convert 3 channel image to 1 channel gray block class
    
    """
    
    def __init__(self):
        super(ipfblock.IPFBlock, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["gray_image"] = ioport.OPort(self, IPFImage1cType)
        self.type = "RGB2Gray"
        self.process_function = processing.rgb2gray

            
        
    
    

