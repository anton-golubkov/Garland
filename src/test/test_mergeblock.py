#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.merge

class TestMergeBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.merge.Merge()
        self.test_image = cv.LoadImage("files/test.png", 0)
        
        
    def test_output_image_channels(self):
        """ Test return to output ports 3 one-channel images of same size
        
        """
        self.block.input_ports["input_image_1"].pass_value(self.test_image)
        self.block.input_ports["input_image_2"].pass_value(self.test_image)
        self.block.input_ports["input_image_3"].pass_value(self.test_image)
        self.block.process()
        out_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(out_image.nChannels, 3)
        
        
    def test_output_image_size(self):
        """ Test return to output port image of same size
        
        """
        self.block.input_ports["input_image_1"].pass_value(self.test_image)
        self.block.input_ports["input_image_2"].pass_value(self.test_image)
        self.block.input_ports["input_image_3"].pass_value(self.test_image)
        self.block.process()
        out_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual((out_image.width, out_image.height), 
                         (self.test_image.width, self.test_image.height))
        
        
    def test_output_image(self):
        self.block.input_ports["input_image_1"].pass_value(self.test_image)
        self.block.input_ports["input_image_2"].pass_value(self.test_image)
        self.block.input_ports["input_image_3"].pass_value(self.test_image)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        cv.SaveImage("files/test_merge_out.png", output_image)
        
        loaded_image = cv.LoadImage("files/test_merge_out.png")
        test_loaded_image = cv.LoadImage("files/test_merge.png")
        self.assertEqual(loaded_image.tostring(), test_loaded_image.tostring())
        
        
    def test_zero_images(self):
        zero_image_1c = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 1)
        self.block.input_ports["input_image_1"].pass_value(zero_image_1c)
        self.block.input_ports["input_image_2"].pass_value(zero_image_1c)
        self.block.input_ports["input_image_3"].pass_value(zero_image_1c)
        self.block.process()
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(output_image.tostring(), zero_image.tostring())
        
    
    def test_one_zero_images(self):
        zero_image_1c = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 1)
        self.block.input_ports["input_image_1"].pass_value(zero_image_1c)
        self.block.input_ports["input_image_2"].pass_value(self.test_image)
        self.block.input_ports["input_image_3"].pass_value(self.test_image)
        self.block.process()
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(output_image.tostring(), zero_image.tostring())
    
    
        
    def test_input_images_diferent_size(self):
        small_image = cv.CreateImage( (50, 50), cv.IPL_DEPTH_8U, 1)
        cv.Resize(self.test_image, small_image)
        self.block.input_ports["input_image_1"].pass_value(small_image)
        self.block.input_ports["input_image_2"].pass_value(self.test_image)
        self.block.input_ports["input_image_3"].pass_value(self.test_image)
        self.block.process()
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(output_image.tostring(), zero_image.tostring())



if __name__ == '__main__':
    unittest.main()
    

