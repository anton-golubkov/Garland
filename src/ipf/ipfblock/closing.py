# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from morphology import Morphology

class Closing(Morphology):
    """ Perform closing filter image 
    
    """
    type = "Closing"
    is_abstract_block = False
    
    def __init__(self):
        super(Closing, self).__init__()
        self.processing_function = ipf.ipfblock.processing.closing
