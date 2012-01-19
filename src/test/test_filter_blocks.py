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
#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.threshold
import ipf.ipfblock.adaptivethreshold
import ipf.ipfblock.threshold_otsu
import ipf.ipfblock.smooth
import ipf.ipfblock.sobel


# Base test class for filters blocks
class TestFilterBlock(unittest.TestCase):
    
    test_class = None
    test_file_name = None
    input_channel_count = None
    output_channel_count = None
    
    def setUp(self):
        if self.test_class is None:
            return
        self.block = self.test_class()
        if self.input_channel_count == 1:
            self.test_image = cv.LoadImage("files/test.png", 0)
        else:
            self.test_image = cv.LoadImage("files/test.png")
        
        self.setup_properties()
        
    
    def setup_properties(self):
        pass 
        
    def test_output_image_channels(self):
        if self.test_class is None:
            return
        """ Test return to output ports n-channel image of same size
        
        """
        self.block.input_ports["input_image"].pass_value(self.test_image)
        self.block.process()
        out_image = self.block.output_ports["output_image"].get_value()
        if self.output_channel_count == 1:
            self.assertEqual(out_image.nChannels, 1)
        else:
            self.assertEqual(out_image.nChannels, 3)
        
        
    def test_output_image_size(self):
        if self.test_class is None:
            return
        """ Test return to output port image of same size
        
        """
        self.block.input_ports["input_image"].pass_value(self.test_image)
        self.block.process()
        out_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual((out_image.width, out_image.height), 
                         (self.test_image.width, self.test_image.height))
        
        
    def test_output_image(self):
        if self.test_class is None:
            return
        self.block.input_ports["input_image"].pass_value(self.test_image)
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
        if self.input_channel_count == 1:
            zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 1)
        else:
            zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.block.input_ports["input_image"].pass_value(zero_image)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        self.assertEqual(output_image.tostring(), zero_image.tostring())
        

class TestThresholdBlock(TestFilterBlock):
    test_class = ipf.ipfblock.threshold.Threshold
    test_file_name = "threshold"
    input_channel_count = 1
    output_channel_count = 1

    def setup_properties(self):
        self.block.properties["threshold_type"].set_value("Binary")
        self.block.properties["threshold"].set_value(127)
        self.block.properties["max_value"].set_value(255)


class TestAdaptiveThresholdBlock(TestFilterBlock):
    test_class = ipf.ipfblock.adaptivethreshold.AdaptiveThreshold
    test_file_name = "adaptive_threshold"
    input_channel_count = 1
    output_channel_count = 1

    def setup_properties(self):
        self.block.properties["threshold_type"].set_value("Binary")
        self.block.properties["adaptive_method"].set_value("Mean")
        self.block.properties["block_size"].set_value("5")
        self.block.properties["param"].set_value(5)
        self.block.properties["max_value"].set_value(255)   


class TestThresholdOtsuBlock(TestFilterBlock):
    test_class = ipf.ipfblock.threshold_otsu.ThresholdOtsu
    test_file_name = "threshold_otsu"
    input_channel_count = 1
    output_channel_count = 1

    def setup_properties(self):
        self.block.properties["threshold_type"].set_value("Binary")
        self.block.properties["max_value"].set_value(255)


class TestSmoothBlock(TestFilterBlock):
    test_class = ipf.ipfblock.smooth.Smooth
    test_file_name = "smooth"
    input_channel_count = 3
    output_channel_count = 3

    def setup_properties(self):
        self.block.properties["smoothing_type"].set_value("Gaussian")
        self.block.properties["aperture_width"].set_value("7")
        self.block.properties["aperture_height"].set_value("9")



class TestSobelBlock(TestFilterBlock):
    test_class = ipf.ipfblock.sobel.Sobel
    test_file_name = "sobel"
    input_channel_count = 3
    output_channel_count = 3

    def setup_properties(self):
        self.block.properties["xorder"].set_value(2)
        self.block.properties["yorder"].set_value(2)
        self.block.properties["kernel_size"].set_value("5")



if __name__ == '__main__':
    unittest.main()
    

