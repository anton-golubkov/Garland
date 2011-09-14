#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

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
        
    def test_create_connection_int(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipfinttype.IPFIntType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipfinttype.IPFIntType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
        
    def test_create_connection_float(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipffloattype.IPFFloatType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipffloattype.IPFFloatType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
        
    def test_create_connection_rgb(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipfrgbtype.IPFRGBType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipfrgbtype.IPFRGBType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
    
    def test_create_connection_image1c(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipfimage1ctype.IPFImage1cType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipfimage1ctype.IPFImage1cType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
    
    def test_create_connection_image3c(self):
        iport = ipf.ipfblock.ioport.IPort(None, ipf.ipftype.ipfimage3ctype.IPFImage3cType())
        oport = ipf.ipfblock.ioport.OPort(None, ipf.ipftype.ipfimage3ctype.IPFImage3cType())
        connection = ipf.ipfblock.connection.Connection(oport, iport)
   
    
            

if __name__ == '__main__':
    unittest.main()
    

