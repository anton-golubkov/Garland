#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.rgb2gray

class TestRGB2GrayBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.rgb2gray.RGB2Gray()
        self.test_image = cv.LoadImage("test.png")
        self.block.input_ports["input_image"].pass_value(self.test_image)
        
        
    def test_output_image_channels(self):
        """ Test return to output port 1 channel image of same size
        
        """
        self.block.process()
        gray_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(gray_image.nChannels, 1)
        
        
    def test_output_image_size(self):
        """ Test return to output port image of same size
        
        """
        self.block.process()
        gray_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual((gray_image.width, gray_image.height), 
                         (self.test_image.width, self.test_image.height))
        
    def test_gray_image(self):
        self.block.process()
        output_gray_image = self.block.output_ports["output_image"].get_value()
        cv.SaveImage("test_gray_out.png", output_gray_image)
        output_gray_image = cv.LoadImage("test_gray_out.png")
        gray_image = cv.LoadImage("test_gray.png")
        self.assertEqual(output_gray_image.tostring(), gray_image.tostring())
        
        
    def test_zero_image(self):
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.block.input_ports["input_image"].pass_value(zero_image)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        zero_image_1c = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 1)
        self.assertEqual(output_image.tostring(), zero_image_1c.tostring())

if __name__ == '__main__':
    unittest.main()
    

