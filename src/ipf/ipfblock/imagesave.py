# -*- coding: utf-8 -*-


import ipfblock
import ioport
import processing
from property import Property
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfstringtype import IPFStringType

class ImageSave(ipfblock.IPFBlock):
    """ Image save block 
    
        Block have 1 input port with type IPFImage3cType 
    """
    
    type = "ImageSave"
    category = "Image I/O"
    
    def __init__(self):
        super(ImageSave, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage3cType)    
        self.processing_function = processing.save_image
        self.properties["file_name"] = Property(IPFStringType)
        
    def get_preview_image(self):
        return self.input_ports["input_image"].value  
