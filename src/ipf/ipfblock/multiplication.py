# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from ipf.ipfblock.arithmetic import Arithmetic

class Multiplication(Arithmetic):
    """ Multiplicate two images 
    
    """
    type = "Multiplication"
    is_abstract_block = False
    
    def __init__(self):
        super(Multiplication, self).__init__()
        self.processing_function = ipf.ipfblock.processing.multiplication


