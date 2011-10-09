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
        self.iplimage = cv.LoadImage("test.png")
        self.pilimage = PIL.Image.open("test.png")
        self.qimage = QtGui.QImage("test.png")
        
        
    def images_equal(self, filename1, filename2):
        i1 = cv.LoadImage(filename1)
        i2 = cv.LoadImage(filename2)
        return i1.tostring() == i2.tostring()
    
    
    def test_ipl_to_pil(self):    
        result_pil = gui.image_convert.iplimage_to_pilimage(self.iplimage)
        result_pil.save("test_ipl_pil.png", "PNG")
        self.assertTrue(self.images_equal("test.png", "test_ipl_pil.png"))
    
    
    def test_pil_to_ipl(self):
        result_ipl = gui.image_convert.pilimage_to_iplimage(self.pilimage)
        cv.SaveImage("test_pil_ipl.png", result_ipl)
        self.assertTrue(self.images_equal("test.png", "test_pil_ipl.png"))
        
        
    def test_qimage_to_ipl(self):
        result_ipl = gui.image_convert.qimage_to_iplimage(self.qimage)
        cv.SaveImage("test_qimage_ipl.png", result_ipl)
        self.assertTrue(self.images_equal("test.png", "test_qimage_ipl.png"))


    def test_pil_to_qimage(self):
        result_qimage = gui.image_convert.pilimage_to_qimage(self.pilimage)
        result_qimage.save("test_pil_qimage.png")
        self.assertTrue(self.images_equal("test.png", "test_pil_qimage.png"))


    def test_qimage_to_pil(self):
        result_pil = gui.image_convert.qimage_to_pilimage(self.qimage)
        result_pil.save("test_qimage_pil.png")
        self.assertTrue(self.images_equal("test.png", "test_qimage_pil.png"))


    def test_ipl_to_qimage(self):
        result_qimage = gui.image_convert.iplimage_to_qimage(self.iplimage)
        result_qimage.save("test_ipl_qimage.png")
        self.assertTrue(self.images_equal("test.png", "test_ipl_qimage.png"))
        
    

if __name__ == '__main__':
    unittest.main()
    

