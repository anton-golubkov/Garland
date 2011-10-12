#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.blackhat

class TestBlackHatBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.blackhat.BlackHat()
        self.test_image = cv.LoadImage("files/test.png")
        self.block.input_ports["input_image"].pass_value(self.test_image)
        self.block.properties["element"].set_value("3x3")
        
        
    def test_output_image_size(self):
        """ Test return to output port image of same size
        
        """
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual((output_image.width, output_image.height), 
                         (self.test_image.width, self.test_image.height))
        
        
    def test_output_image(self):
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        cv.SaveImage("files/test_blackhat_out.png", output_image)
        output_image = cv.LoadImage("files/test_blackhat_out.png")
        erosion_image = cv.LoadImage("files/test_blackhat.png")
        self.assertEqual(output_image.tostring(), erosion_image.tostring())
        
        
    def test_zero_image(self):
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.block.input_ports["input_image"].pass_value(zero_image)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        zero_image_3c = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.assertEqual(output_image.tostring(), zero_image_3c.tostring())


if __name__ == '__main__':
    unittest.main()
    

