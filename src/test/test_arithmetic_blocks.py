#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.sum

# Base test class for arithmetics blocks
class TestArithmeticBlock(unittest.TestCase):
    
    test_class = None
    test_file_name = None

    
    def setUp(self):
        if self.test_class is None:
            return
        self.block = self.test_class()
        self.test_image = cv.LoadImage("files/test.png")
        self.test_image2 = cv.LoadImage("files/test.png", 0)
        
        
    def test_output_image_channels(self):
        if self.test_class is None:
            return
        """ Test return to output ports 3-channel image of same size
        
        """
        self.block.input_ports["input_image_1"].pass_value(self.test_image)
        self.block.input_ports["input_image_2"].pass_value(self.test_image2)
        self.block.process()
        out_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(out_image.nChannels, 3)
        
        
    def test_output_image_size(self):
        if self.test_class is None:
            return
        """ Test return to output port image of same size
        
        """
        self.block.input_ports["input_image_1"].pass_value(self.test_image)
        self.block.input_ports["input_image_2"].pass_value(self.test_image2)
        self.block.process()
        out_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual((out_image.width, out_image.height), 
                         (self.test_image.width, self.test_image.height))
        
        
    def test_output_image(self):
        if self.test_class is None:
            return
        self.block.input_ports["input_image_1"].pass_value(self.test_image)
        self.block.input_ports["input_image_2"].pass_value(self.test_image2)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        cv.SaveImage("files/test_%s_out.png" % (self.test_file_name), 
                     output_image)
        
        loaded_image = cv.LoadImage("files/test_%s_out.png" % (self.test_file_name))
        test_loaded_image = cv.LoadImage("files/test_%s.png" % (self.test_file_name))
        self.assertEqual(loaded_image.tostring(), test_loaded_image.tostring())
        
        
    def test_zero_images(self):
        if self.test_class is None:
            return
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.block.input_ports["input_image_1"].pass_value(zero_image)
        self.block.input_ports["input_image_2"].pass_value(zero_image)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(output_image.tostring(), zero_image.tostring())
        
    
    def test_one_zero_images(self):
        if self.test_class is None:
            return
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.block.input_ports["input_image_1"].pass_value(zero_image)
        self.block.input_ports["input_image_2"].pass_value(self.test_image)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(output_image.tostring(), zero_image.tostring())
    
    
    def test_input_images_diferent_size(self):
        if self.test_class is None:
            return
        small_image = cv.CreateImage( (50, 50), cv.IPL_DEPTH_8U, 3)
        cv.Resize(self.test_image, small_image)
        self.block.input_ports["input_image_1"].pass_value(small_image)
        self.block.input_ports["input_image_2"].pass_value(self.test_image)
        self.block.process()
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(output_image.tostring(), zero_image.tostring())


class TestSumBlock(TestArithmeticBlock):
    test_class = ipf.ipfblock.sum.Sum
    test_file_name = "sum"


if __name__ == '__main__':
    unittest.main()
    

