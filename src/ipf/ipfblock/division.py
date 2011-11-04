# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from ipf.ipfblock.arithmetic import Arithmetic

class Division(Arithmetic):
    """ Divide two images 
    
    """
    type = "Division"
    is_abstract_block = False
    
    def __init__(self):
        super(Division, self).__init__()
        self.processing_function = ipf.ipfblock.processing.divide


