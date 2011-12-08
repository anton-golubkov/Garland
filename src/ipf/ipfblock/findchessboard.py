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
from ipf.ipftype.ipffindchessboardtype import IPFFindChessboardType



class FindChessboard(ipfblock.IPFBlock):
    """ Find chess board corners block
    
    """
    type = "FindChessboard"
    category = "Feature detection"
    is_abstract_block = False
    
    def __init__(self):
        super(FindChessboard, self).__init__()
        self.input_ports["input_image"] = ioport.IPort(self, IPFImage1cType)
        self.output_ports["output_array"] = ioport.OPort(self, IPFArrayType)    
        self.properties["type"] = Property(IPFFindChessboardType)
        self.properties["width"] = Property(IPFIntType, 3, 20)
        self.properties["height"] = Property(IPFIntType, 3, 20)
        self.processing_function = ipf.ipfblock.processing.find_chessboard

    def get_preview_image(self):
        corners = self.output_ports["output_array"]._value
        if len(corners) == 0:
            return self.input_ports["input_image"]._value
        output_image = IPFImage3cType.convert(self.input_ports["input_image"]._value)
        
        width = self.properties["width"].get_value()
        height = self.properties["height"].get_value()
        cv.DrawChessboardCorners(output_image, 
                                 (width, height), 
                                 corners, 
                                 1)
        return output_image         
        
    
    

