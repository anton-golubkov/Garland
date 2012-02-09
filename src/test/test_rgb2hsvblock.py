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


import ipf.ipfblock.rgb2hsv

class TestRGB2HSVBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.rgb2hsv.RGB2HSV()
        self.test_image = cv.LoadImage("files/test.png")
        self.block.input_ports["input_image"].pass_value(self.test_image)
        
        
    def test_output_image_channels(self):
        """ Test return to output ports 3 one-channel images of same size
        
        """
        self.block.process()
        image_1 = self.block.output_ports["output_H"].get_value()
        image_2 = self.block.output_ports["output_S"].get_value()
        image_3 = self.block.output_ports["output_V"].get_value()
        self.assertEqual(image_1.nChannels, 1)
        self.assertEqual(image_2.nChannels, 1)
        self.assertEqual(image_3.nChannels, 1)
        
        
    def test_output_image_size(self):
        """ Test return to output ports images of same size
        
        """
        self.block.process()
        image_1 = self.block.output_ports["output_H"].get_value()
        image_2 = self.block.output_ports["output_S"].get_value()
        image_3 = self.block.output_ports["output_V"].get_value()
        self.assertEqual((image_1.width, image_1.height), 
                         (self.test_image.width, self.test_image.height))
        self.assertEqual((image_2.width, image_2.height), 
                         (self.test_image.width, self.test_image.height))
        self.assertEqual((image_3.width, image_3.height), 
                         (self.test_image.width, self.test_image.height))
        
        
    def test_output_image(self):
        self.block.process()
        output_image_1 = self.block.output_ports["output_H"].get_value()
        output_image_2 = self.block.output_ports["output_S"].get_value()
        output_image_3 = self.block.output_ports["output_V"].get_value()
        cv.SaveImage("files/test_rgb2hsv_out_H.png", output_image_1)
        cv.SaveImage("files/test_rgb2hsv_out_S.png", output_image_2)
        cv.SaveImage("files/test_rgb2hsv_out_V.png", output_image_3)
        
        loaded_image = cv.LoadImage("files/test_rgb2hsv_out_H.png")
        test_loaded_image = cv.LoadImage("files/test_rgb2hsv_H.png")
        self.assertEqual(loaded_image.tostring(), test_loaded_image.tostring())
        
        loaded_image = cv.LoadImage("files/test_rgb2hsv_out_S.png")
        test_loaded_image = cv.LoadImage("files/test_rgb2hsv_S.png")
        self.assertEqual(loaded_image.tostring(), test_loaded_image.tostring())
        
        loaded_image = cv.LoadImage("files/test_rgb2hsv_out_V.png")
        test_loaded_image = cv.LoadImage("files/test_rgb2hsv_V.png")
        self.assertEqual(loaded_image.tostring(), test_loaded_image.tostring())
        
        
    def test_zero_image(self):
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.block.input_ports["input_image"].pass_value(zero_image)
        self.block.process()
        zero_image_1c = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 1)
        output_image_1 = self.block.output_ports["output_H"].get_value()
        output_image_2 = self.block.output_ports["output_S"].get_value()
        output_image_3 = self.block.output_ports["output_V"].get_value()
        self.assertEqual(output_image_1.tostring(), zero_image_1c.tostring())
        self.assertEqual(output_image_2.tostring(), zero_image_1c.tostring())
        self.assertEqual(output_image_3.tostring(), zero_image_1c.tostring())
        


if __name__ == '__main__':
    unittest.main()
    

