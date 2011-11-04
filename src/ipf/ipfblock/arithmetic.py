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
        
    
    

