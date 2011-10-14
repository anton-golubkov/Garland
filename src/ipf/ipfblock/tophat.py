# -*- coding: utf-8 -*-


import ipf.ipfblock.processing
from morphology import Morphology

class TopHat(Morphology):
    """ Perform top hat filter image 
    
    """
    type = "TopHat"
    is_abstract_block = False
    
    def __init__(self):
        super(TopHat, self).__init__()
        self.processing_function = ipf.ipfblock.processing.tophat
        
