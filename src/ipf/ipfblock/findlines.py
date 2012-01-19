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

import cv

import ipfblock
import ioport
import ipf.ipfblock.processing
from property import Property
from ipf.ipftype.ipfimage1ctype import IPFImage1cType
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipfarraytype import IPFArrayType
from ipf.ipftype.ipfinttype import IPFIntType
from ipf.ipftype.ipffloattype import IPFFloatType



class FindLines(ipfblock.IPFBlock):
    """ Find lines block
    
    """
    type = "FindLines"
    category = "Feature detection"
    is_abstract_block = False
    
    def __init__(self):
        super(FindLines, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage1cType)
        self.output_ports["output_array"] = ioport.OPort(self, IPFArrayType)    
        self.properties["distance_resolution"] = Property(IPFIntType, 1, 50)
        self.properties["angle_resolution"] = Property(IPFFloatType, 0.01, 3)
        self.properties["threshold"] = Property(IPFIntType, 1, 255)
        self.properties["min_length"] = Property(IPFIntType, 1, 1000)
        self.properties["max_gap"] = Property(IPFIntType, 1, 1000)
        self.processing_function = ipf.ipfblock.processing.find_lines


    def get_preview_image(self):
        lines = self.output_ports["output_array"]._value
        if len(lines) == 0:
            return self.input_ports["input_image"]._value
        output_image = IPFImage3cType.convert(self.input_ports["input_image"]._value)
        
        for p1, p2 in lines:
            cv.Line(output_image, 
                    p1,
                    p2,
                    (0, 0, 255),
                    3)
        
        return output_image         
        
    
    

