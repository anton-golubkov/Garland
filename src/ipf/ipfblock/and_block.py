# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from ipf.ipfblock.arithmetic import Arithmetic

class And(Arithmetic):
    """ Logical Conjunction of two images 
    
    """
    type = "And"
    is_abstract_block = False
    
    def __init__(self):
        super(And, self).__init__()
        self.processing_function = ipf.ipfblock.processing.conjunction


