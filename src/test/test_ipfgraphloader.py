#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfgraphloader
from ipf.ipfblock.rgb2gray import RGB2Gray
from ipf.ipfblock.imageinput import ImageInput

class TestIPFGraphLoader(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_ipfblock_classes(self):
        block_classes = ipf.ipfgraphloader.get_ipfblock_classes()
        self.assertEqual(block_classes['RGB2Gray'], RGB2Gray)
        self.assertEqual(block_classes['ImageInput'], ImageInput)
    
    def test_load_file(self):
        ipf.ipfgraphloader.load("test.xml")
        
if __name__ == "__main__":
    unittest.main()