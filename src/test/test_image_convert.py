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
import PIL
from PySide import QtGui

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import gui.image_convert

class TestImageConvert(unittest.TestCase):
    
    def setUp(self):
        self.iplimage = cv.LoadImage("files/test.png")
        self.pilimage = PIL.Image.open("files/test.png")
        self.qimage = QtGui.QImage("files/test.png")
        self.gray_iplimage = cv.LoadImage("files/test.png", 0)
        self.zero_iplimage = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3)
        self.zero_pilimage = PIL.Image.Image()
        self.zero_qimage = QtGui.QImage()
        
        
    def images_equal(self, filename1, filename2):
        i1 = cv.LoadImage(filename1)
        i2 = cv.LoadImage(filename2)
        return i1.tostring() == i2.tostring()
    
    
    def test_ipl_to_pil(self):    
        result_pil = gui.image_convert.iplimage_to_pilimage(self.iplimage)
        result_pil.save("files/test_ipl_pil.png", "PNG")
        self.assertTrue(self.images_equal("files/test.png", "files/test_ipl_pil.png"))
    
    
    def test_pil_to_ipl(self):
        result_ipl = gui.image_convert.pilimage_to_iplimage(self.pilimage)
        cv.SaveImage("files/test_pil_ipl.png", result_ipl)
        self.assertTrue(self.images_equal("files/test.png", "files/test_pil_ipl.png"))
        
        
    def test_qimage_to_ipl(self):
        result_ipl = gui.image_convert.qimage_to_iplimage(self.qimage)
        cv.SaveImage("files/test_qimage_ipl.png", result_ipl)
        self.assertTrue(self.images_equal("files/test.png", "files/test_qimage_ipl.png"))


    def test_pil_to_qimage(self):
        result_qimage = gui.image_convert.pilimage_to_qimage(self.pilimage)
        result_qimage.save("files/test_pil_qimage.png")
        self.assertTrue(self.images_equal("files/test.png", "files/test_pil_qimage.png"))


    def test_qimage_to_pil(self):
        result_pil = gui.image_convert.qimage_to_pilimage(self.qimage)
        result_pil.save("files/test_qimage_pil.png")
        self.assertTrue(self.images_equal("files/test.png", "files/test_qimage_pil.png"))


    def test_ipl_to_qimage(self):
        result_qimage = gui.image_convert.iplimage_to_qimage(self.iplimage)
        result_qimage.save("files/test_ipl_qimage.png")
        self.assertTrue(self.images_equal("files/test.png", "files/test_ipl_qimage.png"))
        
        
    def test_zero_ipl_to_pil(self):
        result_pil = gui.image_convert.iplimage_to_pilimage(self.zero_iplimage)
        self.assertEqual(result_pil.size, (0, 0))
        
        
    def test_zero_pil_to_ipl(self):
        result_ipl = gui.image_convert.pilimage_to_iplimage(self.zero_pilimage)
        self.assertEqual(cv.GetSize(result_ipl), (0, 0))
        
        
    def test_zero_ipl_to_q(self):
        result_q = gui.image_convert.iplimage_to_qimage(self.zero_iplimage)
        self.assertEqual(result_q, self.zero_qimage)
        
        
    def test_zero_q_to_ipl(self):
        result_ipl = gui.image_convert.qimage_to_iplimage(self.zero_qimage)
        self.assertEqual(cv.GetSize(result_ipl), (0, 0))
        
        
    def test_zero_pil_to_q(self):
        result_q = gui.image_convert.pilimage_to_qimage(self.zero_pilimage)
        self.assertEqual(result_q, self.zero_qimage)
        
        
    def test_zero_q_to_pil(self):
        result_pil = gui.image_convert.qimage_to_pilimage(self.zero_qimage)
        self.assertEqual(result_pil.size, (0, 0))
        
        
    def test_gray_ipl_to_pil(self):
        result_pil = gui.image_convert.iplimage_to_pilimage(self.gray_iplimage)
        result_pil.save("files/test_gray_ipl_pil.png", "PNG")
        self.assertTrue(self.images_equal("files/test_gray_pil.png", 
                                          "files/test_gray_ipl_pil.png"))
    

if __name__ == '__main__':
    unittest.main()
    

