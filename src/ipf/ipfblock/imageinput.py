# -*- coding: utf-8 -*-



import ipfblock
import ioport
import processing
from ipf.ipfproperty.stringproperty import StringProperty
from ipf.ipftype.ipfimage3ctype import IPFImage3cType


class ImageInput(ipfblock.IPFBlock):
    """ Image input block 
    
        Block have 1 output port with type IPFImage3cType
    """
    
    def __init__(self):
        super(ImageInput, self).__init__()
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage3cType)
        self.type = "ImageInput"
        self.processing_function = processing.load_image
        self.properties["file_name"] = StringProperty()
        
        
