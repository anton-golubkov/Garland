# -*- coding: utf-8 -*-

import ipfblock
import ioport
import ipf.ipfblock.processing
from property import Property
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfinttype import IPFIntType
from ipf.ipftype.ipfelementstype import IPFElementsType


class TopHat(ipfblock.IPFBlock):
    """ Perform top hat filter image 
    
    """
    type = "TopHat"
    category = "Morphological Operations"
    is_abstract_block = False
    
    def __init__(self):
        super(TopHat, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)    
        self.processing_function = ipf.ipfblock.processing.tophat
        self.properties["element"] = Property(IPFElementsType)

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
    
    

