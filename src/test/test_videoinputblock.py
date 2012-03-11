#-------------------------------------------------------------------------------
# Copyright (c) 2011-2012 Anton Golubkov.
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


import ipf.ipfblock.videoinput
import ipf.ipfblock.processing

class TestVideoInputBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.videoinput.VideoInput()
        self.block.properties["file_name"].set_value("files/in.avi")
        self.block.properties["frame"].set_value(0)
        self.block.properties["frame_shift"].set_value(0)
    
        
    def test_load_image(self):
        """ Test load video from file 
        
        """
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        cv.SaveImage("files/test_video0_out.png", output_image)
        loaded_image = cv.LoadImage("files/test_video0_out.png")
        test_loaded_image = cv.LoadImage("files/test_video0.png")
        self.assertEqual(loaded_image.tostring(), test_loaded_image.tostring())
        
        
    def test_load_image_frame(self):
        """ Test load video from file for 10 frame 
        
        """
        self.block.properties["frame"].set_value(10)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        cv.SaveImage("files/test_video10_out.png", output_image)
        loaded_image = cv.LoadImage("files/test_video10_out.png")
        test_loaded_image = cv.LoadImage("files/test_video10.png")
        self.assertEqual(loaded_image.tostring(), test_loaded_image.tostring())        

    def test_load_image_frame_shift(self):
        """ Test load video from file for 5 frame with shift 5 
        
        """
        self.block.properties["frame"].set_value(5)
        self.block.properties["frame_shift"].set_value(5)
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        cv.SaveImage("files/test_video10_shift_out.png", output_image)
        loaded_image = cv.LoadImage("files/test_video10_shift_out.png")
        test_loaded_image = cv.LoadImage("files/test_video10.png")
        self.assertEqual(loaded_image.tostring(), test_loaded_image.tostring())
        
        
    def test_no_image_loaded(self):
        self.block.properties["file_name"].set_value("")
        self.block.process()
        output_image = self.block.output_ports["output_image"].get_value()
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.assertEqual(output_image.tostring(), zero_image.tostring())
        
        
    def test_capture_object_error_wrong_name(self):
        """ Test error opening capture object for wrong file name
        
        """
        
        # Test for wrong file name
        capture = ipf.ipfblock.processing.CaptureObject("wrong_filename.avi")
        self.assertTrue(capture.error_open)
    
    
    def test_capture_object_error_empty_name(self):
        """ Test error opening capture object for Test empty file name
        
        """
        capture = ipf.ipfblock.processing.CaptureObject("")
        self.assertTrue(capture.error_open)
        
    
    def test_capture_object_no_error_ok_name(self):
        """ Test opening capture object for normal file name
        
        """
        capture = ipf.ipfblock.processing.CaptureObject("files/in.avi")
        self.assertFalse(capture.error_open)
        
        
        

if __name__ == '__main__':
    unittest.main()
    

