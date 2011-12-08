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
from property import Property
from ipf.ipftype.ipfinttype import IPFIntType
from morphology import Morphology


class Dilate(Morphology):
    """ Dilate image 
    
    """
    type = "Dilate"
    is_abstract_block = False
    
    def __init__(self):
        super(Dilate, self).__init__()
        self.processing_function = ipf.ipfblock.processing.dilate
        self.properties["iterations"] = Property(IPFIntType, 1, 50)
    

