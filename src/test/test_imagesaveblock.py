#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.imagesave

class TestImageSaveBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.imagesave.ImageSave()
        self.block.properties["file_name"].value = "test_saved.png"
    
        
    def test_save_image(self):
        """ Test save image to file 
        
        """
        image = cv.LoadImage("test.png")
        self.block.input_ports["input_image"].pass_value(image)
        self.block.process()
        saved_image = cv.LoadImage("test_saved.png")
        self.assertEqual(saved_image.tostring(), image.tostring())
            

if __name__ == '__main__':
    unittest.main()
    

