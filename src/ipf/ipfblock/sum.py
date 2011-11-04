# -*- coding: utf-8 -*-

import ipf.ipfblock.processing
from ipf.ipfblock.arithmetic import Arithmetic

class Sum(Arithmetic):
    """ Summarize two images 
    
    """
    type = "Sum"
    is_abstract_block = False
    
    def __init__(self):
        super(Sum, self).__init__()
        self.processing_function = ipf.ipfblock.processing.sum


