#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.connection
import ipf.ipfblock.ioport
import ipf.ipftype.ipfinttype
import ipf.ipftype.ipfimage1ctype
import ipf.ipftype.ipfimage3ctype
import ipf.ipftype.ipffloattype
import ipf.ipftype.ipfrgbtype


class TestConnection(unittest.TestCase):
    def setUp(self):
        pass
        
    def test_connection_int(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipfinttype.IPFIntType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipfinttype.IPFIntType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
        self.assertEqual(oport._binded_count, 1)
        self.assertFalse(iport.is_free())
        oport._set_value(42)
        connection.process()
        transmitted_value = iport._get_value()
        self.assertEqual(transmitted_value, 42)
        del connection
        self.assertEqual(oport._binded_count, 0)
        self.assertTrue(iport.is_free())
        
        
    def test_connection_float(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipffloattype.IPFFloatType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipffloattype.IPFFloatType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
        self.assertEqual(oport._binded_count, 1)
        self.assertFalse(iport.is_free())
        oport._set_value(1.1)
        connection.process()
        transmitted_value = iport._get_value()
        self.assertEqual(transmitted_value, 1.1)
        del connection
        self.assertEqual(oport._binded_count, 0)
        self.assertTrue(iport.is_free())
        
        
    def test_connection_rgb(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipfrgbtype.IPFRGBType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipfrgbtype.IPFRGBType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
        self.assertEqual(oport._binded_count, 1)
        self.assertFalse(iport.is_free())
        oport._set_value([127, 127, 127])
        connection.process()
        transmitted_value = iport._get_value()
        self.assertEqual(transmitted_value, [127, 127, 127])
        del connection
        self.assertEqual(oport._binded_count, 0)
        self.assertTrue(iport.is_free())
    
    
    def test_connection_image1c(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipfimage1ctype.IPFImage1cType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipfimage1ctype.IPFImage1cType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
        self.assertEqual(oport._binded_count, 1)
        self.assertFalse(iport.is_free())
        image = cv.LoadImage("files/test.png", 0)
        oport._set_value(image)
        connection.process()
        transmitted_value = iport._get_value()
        self.assertEqual(transmitted_value, image)
        del connection
        self.assertEqual(oport._binded_count, 0)
        self.assertTrue(iport.is_free())
    
    
    def test_connection_image3c(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipfimage3ctype.IPFImage3cType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipfimage3ctype.IPFImage3cType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
        self.assertEqual(oport._binded_count, 1)
        self.assertFalse(iport.is_free())
        image = cv.LoadImage("files/test.png")
        oport._set_value(image)
        connection.process()
        transmitted_value = iport._get_value()
        self.assertEqual(transmitted_value, image)
        del connection
        self.assertEqual(oport._binded_count, 0)
        self.assertTrue(iport.is_free())
   
   
    def test_connection_image_1c_3c(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipfimage3ctype.IPFImage3cType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipfimage1ctype.IPFImage1cType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
        self.assertEqual(oport._binded_count, 1)
        self.assertFalse(iport.is_free())
        image = cv.LoadImage("files/test.png", 0)
        oport._set_value(image)
        connection.process()
        transmitted_value = iport._get_value()
        image1c = cv.CreateImage(cv.GetSize(transmitted_value), cv.IPL_DEPTH_8U, 1)
        cv.Split(transmitted_value, image1c, None, None, None)
        self.assertEqual(image1c.tostring(), image.tostring())
        del connection
        self.assertEqual(oport._binded_count, 0)
        self.assertTrue(iport.is_free())
        
    
            

if __name__ == '__main__':
    unittest.main()
    

