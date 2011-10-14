# -*- coding: utf-8 -*-


import ipf.ipfblock.processing
from property import Property
from ipf.ipftype.ipfinttype import IPFIntType
from morphology import Morphology


class Erosion(Morphology):
    """ Erode image 
    
    """
    type = "Erosion"
    is_abstract_block = False
    
    def __init__(self):
        super(Erosion, self).__init__()
        self.processing_function = ipf.ipfblock.processing.erosion
        self.properties["iterations"] = Property(IPFIntType, 1, 50)

