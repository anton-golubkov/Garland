#-------------------------------------------------------------------------------
# Copyright (c) 2011 - 2012 Anton Golubkov.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Lesser Public License v2.1
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     Anton Golubkov - initial API and implementation
#-------------------------------------------------------------------------------
#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.matchtemplate

class TestMatchTemplateBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.matchtemplate.MatchTemplate()
        self.test_image = cv.LoadImage("files/test.png")
        self.template = cv.LoadImage("files/chess.jpg")
        self.block.input_ports["input_image"].pass_value(self.test_image)
        self.block.input_ports["input_template"].pass_value(self.template)
        self.block.properties["method"].set_value("CV_TM_CCOEFF")
        
        
    def test_output_image_channels(self):
        """ Test return to output port 1-channel image 
        
        """
        self.block.process()
        out_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(out_image.nChannels, 1)
        
        
    def test_output_image_size(self):
        """ Test return to output port image with size (W - w + 1, H - h + 1)
            where W, H - input image size; w,h - template image size
        
        """
        self.block.process()
        out_image = self.block.output_ports["output_image"].get_value()
        W, H = cv.GetSize(self.test_image)
        w, h = cv.GetSize(self.template)
        out_size = (W - w + 1, H - h + 1) 
        self.assertEqual( cv.GetSize(out_image), out_size)
        
    
    def test_result_image(self):
        """ Compare result image with reference image  
        
        """
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        cv.SaveImage("files/test_match_template_out.png", output_image)
        loaded_image = cv.LoadImage("files/test_match_template_out.png")
        test_loaded_image = cv.LoadImage("files/test_match_template.png")
        self.assertEqual(loaded_image.tostring(), test_loaded_image.tostring())
        
        
    def test_image_template_equal_size(self):
        """ If image and template have same size, then output image is 1x1 size
        
        """
        self.block.input_ports["input_template"].pass_value(self.test_image)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual( cv.GetSize(output_image), (1, 1))
        
    
    def test_template_bigger_than_image(self):
        """ If template image are bigger than input image then result is zero image 
        
        """
        self.block.input_ports["input_template"].pass_value(self.test_image)
        self.block.input_ports["input_image"].pass_value(self.template)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.assertEqual(output_image.tostring(), zero_image.tostring())
        
        
    def test_zero_image(self):
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.block.input_ports["input_image"].pass_value(zero_image)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(output_image.tostring(), zero_image.tostring())

        
    def test_zero_template(self):
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.block.input_ports["input_template"].pass_value(zero_image)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        zero_image_3c = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.assertEqual(output_image.tostring(), zero_image_3c.tostring())

if __name__ == '__main__':
    unittest.main()
    

