# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from ipf.ipfblock.arithmetic import Arithmetic

class Subtract(Arithmetic):
    """ Subtract two images 
    
    """
    type = "Subtract"
    is_abstract_block = False
    
    def __init__(self):
        super(Subtract, self).__init__()
        self.processing_function = ipf.ipfblock.processing.subtract


