# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from morphology import Morphology

class BlackHat(Morphology):
    """ Perform black hat filter image 
    
    """
    type = "BlackHat"
    is_abstract_block = False
    
    def __init__(self):
        super(BlackHat, self).__init__()
        self.processing_function = ipf.ipfblock.processing.blackhat
    
