#-------------------------------------------------------------------------------
# Copyright (c) 2011 Anton Golubkov.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Lesser Public License v2.1
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     Anton Golubkov - initial API and implementation
#-------------------------------------------------------------------------------
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
