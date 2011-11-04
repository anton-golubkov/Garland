# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from ipf.ipfblock.arithmetic import Arithmetic

class Or(Arithmetic):
    """ Logical  Disjunction of two images 
    
    """
    type = "Or"
    is_abstract_block = False
    
    def __init__(self):
        super(Or, self).__init__()
        self.processing_function = ipf.ipfblock.processing.disjunction


