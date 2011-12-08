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


import ipf.ipfblock.imagesave

class TestImageSaveBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.imagesave.ImageSave()
        self.block.properties["file_name"].set_value("files/test_saved.png")
    
        
    def test_save_image(self):
        """ Test save image to file 
        
        """
        image = cv.LoadImage("files/test.png")
        self.block.input_ports["input_image"].pass_value(image)
        self.block.process()
        saved_image = cv.LoadImage("files/test_saved.png")
        self.assertEqual(saved_image.tostring(), image.tostring())
        
        
    def tearDown(self):
        os.remove("files/test_saved.png")
            

if __name__ == '__main__':
    unittest.main()
    

