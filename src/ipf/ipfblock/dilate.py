# -*- coding: utf-8 -*-

import ipfblock
import ioport
import ipf.ipfblock.processing
from property import Property
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfinttype import IPFIntType
from ipf.ipftype.ipfelementstype import IPFElementsType


class Dilate(ipfblock.IPFBlock):
    """ Dilate image 
    
    """
    type = "Dilate"
    category = "Morphological Operations"
    
    def __init__(self):
        super(Dilate, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)    
        self.processing_function = ipf.ipfblock.processing.dilate
        self.properties["element"] = Property(IPFElementsType)
        self.properties["iterations"] = Property(IPFIntType, 1, 50)

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
    
    

