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
from ipf.ipftype.ipfstringtype import IPFStringType
from ipf.ipfblock.property import Property

class TestProperty(unittest.TestCase):
    
    def setUp(self):
        self.property_int = Property(IPFIntType)
        self.property_int_limits = Property(IPFIntType, 0, 100)
        self.property_float = Property(IPFFloatType)
        self.property_float_limits = Property(IPFFloatType, 0.0, 100.0)
        self.property_rgb = Property(IPFRGBType)
        self.property_string = Property(IPFStringType)
        
    
    def test_set_get_value(self):    
        self.property_int.set_value(135)
        self.assertEqual(self.property_int.get_value(), 135)
        
        self.property_int_limits.set_value(42)
        self.assertEqual(self.property_int_limits.get_value(), 42)
        
        self.property_float.set_value(135.5)
        self.assertEqual(self.property_float.get_value(), 135.5)
        
        self.property_float_limits.set_value(42.5)
        self.assertEqual(self.property_float_limits.get_value(), 42.5)
        
        self.property_rgb.set_value([42, 42, 42])
        self.assertEqual(self.property_rgb.get_value(), [42, 42, 42])
        
        self.property_string.set_value("testing string")
        self.assertEqual(self.property_string.get_value(), "testing string")
        
        
        
    def test_set_get_limit_value(self):
        self.assertRaises(ValueError, self.property_int_limits.set_value, -200 )
        self.assertRaises(ValueError, self.property_int_limits.set_value, 200 )
        
        self.assertRaises(ValueError, self.property_float_limits.set_value, -200.5 )
        self.assertRaises(ValueError, self.property_float_limits.set_value, 200.5 )
        
        
if __name__ == '__main__':
    unittest.main()
    

