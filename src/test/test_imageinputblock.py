#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.imageinput

class TestImageInputBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.imageinput.ImageInput()
        self.block.properties["file_name"].value = "test.png"
    
        
    def test_load_image(self):
        """ Test load image from file 
        
        """
        self.block.execute()
        loaded_image = self.block.output_ports["output_image"].get_value()
        test_image = cv.LoadImage("test.png")
        self.assertEqual(loaded_image.tostring(), test_image.tostring())
            

if __name__ == '__main__':
    unittest.main()
    

