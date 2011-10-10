#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

import ipf.ipftype.ipfinttype
import ipf.ipftype.ipfimage1ctype
import ipf.ipftype.ipfimage3ctype
import ipf.ipftype.ipffloattype
import ipf.ipftype.ipfrgbtype


class TestIPFType(unittest.TestCase):
    def setUp(self):
        self.int1 = ipf.ipftype.ipfinttype.IPFIntType()
        self.int2 = ipf.ipftype.ipfinttype.IPFIntType()
        self.float1 = ipf.ipftype.ipffloattype.IPFFloatType()
        self.float2 = ipf.ipftype.ipffloattype.IPFFloatType()
        self.rgb1 = ipf.ipftype.ipfrgbtype.IPFRGBType()
        self.rgb2 = ipf.ipftype.ipfrgbtype.IPFRGBType()
        self.image3c1 = ipf.ipftype.ipfimage3ctype.IPFImage3cType()
        self.image3c2 = ipf.ipftype.ipfimage3ctype.IPFImage3cType()
        self.image1c1 = ipf.ipftype.ipfimage1ctype.IPFImage1cType()
        self.image1c2 = ipf.ipftype.ipfimage1ctype.IPFImage1cType()
        
        
    def test_compatible_types(self):
        self.assertTrue(self.int1.is_compatible(self.int2))
        self.assertTrue(self.float1.is_compatible(self.float2))
        self.assertTrue(self.rgb1.is_compatible(self.rgb2))
        self.assertTrue(self.image3c1.is_compatible(self.image3c2))
        self.assertTrue(self.image1c1.is_compatible(self.image1c2))
        self.assertTrue(self.image3c1.is_compatible(self.image1c1))
        self.assertTrue(self.int1.is_compatible(self.float1))
        self.assertTrue(self.float1.is_compatible(self.int1))
        
        
    def test_uncompatible_types(self):
        self.assertFalse(self.int1.is_compatible(self.rgb1))
        self.assertFalse(self.int1.is_compatible(self.image1c1))
        self.assertFalse(self.int1.is_compatible(self.image3c1))
        self.assertFalse(self.rgb1.is_compatible(self.float1))
        self.assertFalse(self.rgb1.is_compatible(self.image1c1))
        self.assertFalse(self.rgb1.is_compatible(self.image3c1))
    
    
    def test_convert_types(self):
        self.assertEqual(10, self.int1.convert(10))
        self.assertEqual(10, self.int1.convert(10.1))
        self.assertEqual(10.1, self.float1.convert(10.1))
        self.assertEqual(10.0, self.float1.convert(10))
        self.assertEqual([255, 255, 255], self.rgb1.convert([255,255,255]))
        self.assertEqual([255, 255, 255], self.rgb1.convert((255,255,255)))
        
        
        i1c = cv.LoadImage("files/test.png", 0)
        i3c = cv.LoadImage("files/test.png")
        
        i3c_gray = cv.CreateImage(cv.GetSize(i1c), cv.IPL_DEPTH_8U, 3)
        cv.Merge(i1c, i1c, i1c, None, i3c_gray)
        
        self.assertEqual(i1c, self.image1c1.convert(i1c))
        self.assertEqual(i3c, self.image3c1.convert(i3c))
        self.assertEqual(i3c_gray.tostring(), self.image3c1.convert(i1c).tostring())
        
        
        
    

if __name__ == '__main__':
    unittest.main()
    

