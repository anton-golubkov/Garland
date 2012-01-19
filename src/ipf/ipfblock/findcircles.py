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




class FindCircles(ipfblock.IPFBlock):
    """ Find circles block
    
    """
    type = "FindCircles"
    category = "Feature detection"
    is_abstract_block = False
    
    def __init__(self):
        super(FindCircles, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage1cType)
        self.output_ports["output_array"] = ioport.OPort(self, IPFArrayType)    
        self.properties["accum_divider"] = Property(IPFIntType, 1, 4)
        self.properties["min_distance"] = Property(IPFIntType, 1, 1000)
        self.properties["threshold"] = Property(IPFIntType, 1, 255)
        self.properties["accum_threshold"] = Property(IPFIntType, 1, 255)
        self.properties["min_radius"] = Property(IPFIntType, 1, 1000)
        self.properties["max_radius"] = Property(IPFIntType, 1, 1000)
        self.processing_function = ipf.ipfblock.processing.find_circles


    def get_preview_image(self):
        circles = self.output_ports["output_array"]._value
        if len(circles) == 0:
            return self.input_ports["input_image"]._value
        output_image = IPFImage3cType.convert(self.input_ports["input_image"]._value)
        
        for x, y, r in circles:
            cv.Circle(output_image, ( int(x), int(y)), int(r), (0, 0, 255))
        
        return output_image         
        
    
    

