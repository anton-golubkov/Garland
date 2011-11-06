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
    
    
    def test_load_and_save_files(self):
        test_files = ["test",
                      "test_cells",
                      "test_large",]
        for file_name in test_files:
            self.help_test_load_and_save_file(file_name)
        
    
    def help_test_load_and_save_file(self, file_name):
        graph = ipf.ipfgraphloader.load("files/%s.xml" % (file_name))
        graph.save("files/%s_load_save.xml" % (file_name))
        self.assertTrue(filecmp.cmp("files/%s_load_save.xml" % (file_name),
                                    "files/%s.xml" % (file_name) ),
                                    "Load save failed: %s" % (file_name)) 
        
if __name__ == "__main__":
    unittest.main()