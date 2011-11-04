# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from ipf.ipfblock.arithmetic import Arithmetic


import ipfblock
import ioport
import ipf.ipfblock.processing
from ipf.ipftype.ipfimage3ctype import IPFImage3cType


class Not(ipfblock.IPFBlock):
    """ Logical Not block (inverts image)  
    
    """
    type = "Not"
    category = "Arithmetic and logic"
    is_abstract_block = False
    
    def __init__(self):
        super(Not, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)
        self.processing_function = ipf.ipfblock.processing.invert

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
        

        


