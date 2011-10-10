#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import filecmp

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
    
    def test_load_and_save_file(self):
        graph = ipf.ipfgraphloader.load("files/test.xml")
        graph.save("files/test_load_save.xml")
        self.assertTrue(filecmp.cmp("files/test_load_save.xml", "files/test.xml"))
        
        
if __name__ == "__main__":
    unittest.main()