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


import ipf.ipfblock.findcircles

class TestFindCirclesBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.findcircles.FindCircles()
        self.block.properties["max_radius"].set_value(300)
        self.block.properties["min_radius"].set_value(1)
        self.block.properties["threshold"].set_value(80)
        self.block.properties["accum_divider"].set_value(1)
        self.block.properties["accum_threshold"].set_value(70)
        self.block.properties["min_distance"].set_value(20)
        
        
    def test_zero_image(self):
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 1)
        self.block.input_ports["input_image"].pass_value(zero_image)
        self.block.process()
        output_array = self.block.output_ports["output_array"].get_value()
        self.assertTrue(output_array ==  [])
        
    
    def test_no_circles(self):
        image = cv.LoadImage("files/chess.jpg")
        gray_image = cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_8U, 1)
        cv.CvtColor(image, gray_image, cv.CV_RGB2GRAY)
        self.block.input_ports["input_image"].pass_value(gray_image)
        self.block.process()
        output_array = self.block.output_ports["output_array"].get_value()
        self.assertTrue(output_array ==  [])
        
    
    def test_find_circles(self):
        image = cv.LoadImage("files/circles.jpg")
        gray_image = cv.CreateImage(cv.GetSize(image), cv.IPL_DEPTH_8U, 1)
        cv.CvtColor(image, gray_image, cv.CV_RGB2GRAY)
        self.block.input_ports["input_image"].pass_value(gray_image)
        self.block.process()
        output_array = self.block.output_ports["output_array"].get_value()
        self.assertTrue(len(output_array) == 4)
        


if __name__ == '__main__':
    unittest.main()
    

