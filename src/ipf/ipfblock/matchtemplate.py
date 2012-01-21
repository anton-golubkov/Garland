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
from ipf.ipfblock.arithmetic import Arithmetic
from ipf.ipftype.ipfimage1ctype import IPFImage1cType
import ioport
from ipf.ipftype.ipfmatchtemplatemethodtype import IPFMatchTemplateMethodType
from property import Property

class MatchTemplate(Arithmetic):
    """ Calculate template correlation map 
    
    """
    type = "MatchTemplate"
    category = "Feature detection"
    is_abstract_block = False
    
    def __init__(self):
        super(MatchTemplate, self).__init__()
        self.output_ports["output_image"] = ioport.OPort(self, IPFImage1cType)
        self.properties["method"] = Property(IPFMatchTemplateMethodType)
        self.processing_function = ipf.ipfblock.processing.match_template


