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
        gray_image = self.block.output_ports["gray_image"].get_value()
        self.assertEqual(gray_image.nChannels, 1)
        
    def test_output_image_size(self):
        """ Test return to output port image of same size
        
        """
        self.block.process()
        gray_image = self.block.output_ports["gray_image"].get_value()
        self.assertEqual((gray_image.width, gray_image.height), 
                         (self.test_image.width, self.test_image.height))
        

if __name__ == '__main__':
    unittest.main()
    

