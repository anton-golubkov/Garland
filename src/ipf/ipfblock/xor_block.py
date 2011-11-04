# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from ipf.ipfblock.arithmetic import Arithmetic

class Xor(Arithmetic):
    """ Logical  Xor of two images 
    
    """
    type = "Xor"
    is_abstract_block = False
    
    def __init__(self):
        super(Xor, self).__init__()
        self.processing_function = ipf.ipfblock.processing.xor


