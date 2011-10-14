# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from property import Property
from ipf.ipftype.ipfinttype import IPFIntType
from morphology import Morphology


class Dilate(Morphology):
    """ Dilate image 
    
    """
    type = "Dilate"
    is_abstract_block = False
    
    def __init__(self):
        super(Dilate, self).__init__()
        self.processing_function = ipf.ipfblock.processing.dilate
        self.properties["iterations"] = Property(IPFIntType, 1, 50)
    

