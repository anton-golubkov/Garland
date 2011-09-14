#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipf
import ipf.ipfblock.rgb2gray
import ipf.ipfblock.imageinput


class TestIPFGraph(unittest.TestCase):

    def setUp(self):
        self.ipf_graph = ipf.ipf.IPFGraph()
        self.input_block = ipf.ipfblock.imageinput.ImageInput()
        self.rgb2gray_block = ipf.ipfblock.rgb2gray.RGB2Gray()
        self.input_block.properties["file_name"].value = "test.png"

    def test_add_block(self):
        self.ipf_graph.add_block("input_image", self.input_block)
        self.ipf_graph.add_block("rgb2gray1", self.rgb2gray_block)
        self.assertTrue("input_image" in self.ipf_graph.blocks.keys())
        self.assertTrue("rgb2gray1" in self.ipf_graph.blocks.keys())
        
    def test_remove_block(self):
        self.ipf_graph.add_block("input_image", self.input_block)
        self.ipf_graph.add_block("rgb2gray1", self.rgb2gray_block)
        self.ipf_graph.remove_block("input_image")
        self.assertFalse("input_image" in self.ipf_graph.blocks.keys())
        self.ipf_graph.remove_block("rgb2gray1")
        self.assertFalse("rgb2gray1" in self.ipf_graph.blocks.keys())
        self.assertTrue(len(self.ipf_graph.blocks) == 0)
    
    def test_add_connection(self):
        self.ipf_graph.add_block("input_image", self.input_block)
        self.ipf_graph.add_block("rgb2gray1", self.rgb2gray_block)
        oport = self.input_block.output_ports["output_image"]
        iport = self.rgb2gray_block.input_ports["input_image"]
        self.ipf_graph.add_connection(oport, iport)
        self.assertEqual(len(self.ipf_graph.connections), 1 )
        connection = self.ipf_graph.connections[0]
        self.assertEqual(connection._oport, oport)
        self.assertEqual(connection._iport, iport)
        
    
    def test_process(self):
        pass


if __name__ == "__main__":
    unittest.main()