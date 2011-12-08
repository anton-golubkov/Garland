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


import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


from ipf.ipftype.ipfinttype import IPFIntType
from ipf.ipftype.ipfimage1ctype import IPFImage1cType
from ipf.ipftype.ipfimage3ctype import IPFImage3cType
from ipf.ipftype.ipffloattype import IPFFloatType
from ipf.ipftype.ipfrgbtype import IPFRGBType
from ipf.ipfblock.ioport import IPort, OPort, compatible

class TestIOPort(unittest.TestCase):
    
    def setUp(self):
        self.iport_int = IPort(ipfblock=None, data_type=IPFIntType())
        self.iport_float = IPort(ipfblock=None, data_type=IPFFloatType())
        self.iport_image1c = IPort(ipfblock=None, data_type=IPFImage1cType())
        self.iport_image3c = IPort(ipfblock=None, data_type=IPFImage3cType())
        self.iport_rgb = IPort(ipfblock=None, data_type=IPFRGBType())
        
        self.oport_int = OPort(ipfblock=None, data_type=IPFIntType())
        self.oport_float = OPort(ipfblock=None, data_type=IPFFloatType())
        self.oport_image1c = OPort(ipfblock=None, data_type=IPFImage1cType())
        self.oport_image3c = OPort(ipfblock=None, data_type=IPFImage3cType())
        self.oport_rgb = OPort(ipfblock=None, data_type=IPFRGBType())
        
    
    def test_same_type_compatibility(self):    
        self.assertTrue(compatible(self.iport_int, self.oport_int) )
        self.assertTrue(compatible(self.iport_float, self.oport_float) )
        self.assertTrue(compatible(self.iport_image1c, self.oport_image1c) )
        self.assertTrue(compatible(self.iport_image3c, self.oport_image3c) )
        self.assertTrue(compatible(self.iport_rgb, self.oport_rgb) )
        
        self.assertTrue(compatible(self.oport_int, self.iport_int) )
        self.assertTrue(compatible(self.oport_float, self.iport_float) )
        self.assertTrue(compatible(self.oport_image1c, self.iport_image1c) )
        self.assertTrue(compatible(self.oport_image3c, self.iport_image3c) )
        self.assertTrue(compatible(self.oport_rgb, self.iport_rgb) )
            
    
    def test_different_type_compatibility(self):
        self.assertTrue(compatible(self.iport_int, self.oport_float) )
        self.assertTrue(compatible(self.iport_float, self.oport_int) )
        
        self.assertTrue(compatible(self.oport_int, self.iport_float) )
        self.assertTrue(compatible(self.oport_float, self.iport_int) )
        
        # Allow convert from 1 channel to 3 channel
        self.assertTrue(compatible(self.oport_image1c, self.iport_image3c) )


    def test_different_type_uncompatibility(self):
        self.assertFalse(compatible(self.iport_int, self.oport_image1c) )
        self.assertFalse(compatible(self.iport_float, self.oport_image1c) )
        self.assertFalse(compatible(self.iport_image1c, self.oport_image3c) )
        self.assertFalse(compatible(self.iport_int, self.oport_rgb) )
        self.assertFalse(compatible(self.iport_rgb, self.oport_float) )
        
        self.assertFalse(compatible(self.oport_int, self.iport_image1c) )
        self.assertFalse(compatible(self.oport_float, self.iport_image1c) )
        self.assertFalse(compatible(self.oport_int, self.iport_rgb) )
        self.assertFalse(compatible(self.oport_rgb, self.iport_float) )


    def test_iport_uncompatibility(self):
        self.assertFalse(compatible(self.iport_int, self.iport_int) )
        self.assertFalse(compatible(self.iport_float, self.iport_float) )
        self.assertFalse(compatible(self.iport_image1c, self.iport_image1c) )
        self.assertFalse(compatible(self.iport_image3c, self.iport_image3c) )
        self.assertFalse(compatible(self.iport_rgb, self.iport_rgb) )
        
        self.assertFalse(compatible(self.oport_int, self.oport_int) )
        self.assertFalse(compatible(self.oport_float, self.oport_float) )
        self.assertFalse(compatible(self.oport_image1c, self.oport_image1c) )
        self.assertFalse(compatible(self.oport_image3c, self.oport_image3c) )
        self.assertFalse(compatible(self.oport_rgb, self.oport_rgb) )

    def test_compatibly_argument_swap(self):
        self.assertTrue(compatible(self.oport_image1c, self.iport_image3c) )
        self.assertTrue(compatible(self.iport_image3c, self.oport_image1c) )
        
        self.assertTrue(compatible(self.iport_int, self.oport_float) )
        self.assertTrue(compatible(self.oport_float, self.iport_int) )
        
        self.assertTrue(compatible(self.iport_float, self.oport_int) )
        self.assertTrue(compatible(self.oport_int, self.iport_float) )
        
        self.assertTrue(compatible(self.oport_int, self.iport_float) )
        self.assertTrue(compatible(self.iport_float, self.oport_int) )
        
        self.assertTrue(compatible(self.oport_float, self.iport_int) )
        self.assertTrue(compatible(self.iport_int, self.oport_float) )

if __name__ == '__main__':
    unittest.main()
    

