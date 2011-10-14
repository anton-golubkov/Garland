#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv
import filecmp

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfgraph
import ipf.ipfblock.rgb2gray
import ipf.ipfblock.imageinput
import ipf.ipfgraphloader


class TestIPFGraph(unittest.TestCase):

    def setUp(self):
        self.ipf_graph = ipf.ipfgraph.IPFGraph()
        self.input_block = ipf.ipfblock.imageinput.ImageInput()
        self.rgb2gray_block = ipf.ipfblock.rgb2gray.RGB2Gray()
        self.input_block.properties["file_name"].set_value("files/test.png")

    
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
        for connection in self.ipf_graph.connections:
            self.assertEqual(connection._oport, oport)
            self.assertEqual(connection._iport, iport)
    
    
    def test_delete_block_with_connections(self):
        self.ipf_graph.add_block("input_image", self.input_block)
        self.ipf_graph.add_block("rgb2gray1", self.rgb2gray_block)
        oport = self.input_block.output_ports["output_image"]
        iport = self.rgb2gray_block.input_ports["input_image"]
        self.ipf_graph.add_connection(oport, iport)
        self.ipf_graph.remove_block("input_image")
        self.assertEqual(len(self.ipf_graph.connections), 0 )
        
    
    def test_process(self):
        self.ipf_graph.add_block("input_image", self.input_block)
        self.ipf_graph.add_block("rgb2gray1", self.rgb2gray_block)
        oport = self.input_block.output_ports["output_image"]
        iport = self.rgb2gray_block.input_ports["input_image"]
        self.ipf_graph.add_connection(oport, iport)
        self.ipf_graph.process()
        # This flow must return gray image
        test_image = cv.LoadImage("files/test.png")
        gray_image = cv.CreateImage(cv.GetSize(test_image), cv.IPL_DEPTH_8U, 1)
        cv.CvtColor(test_image, gray_image, cv.CV_RGB2GRAY)
        processed_image = self.rgb2gray_block.output_ports["output_image"].get_value() 
        self.assertEqual(processed_image.tostring(), gray_image.tostring())
        
    
    def test_save(self):
        self.ipf_graph.add_block("input_image", self.input_block)
        self.ipf_graph.add_block("rgb2gray1", self.rgb2gray_block)
        oport = self.input_block.output_ports["output_image"]
        iport = self.rgb2gray_block.input_ports["input_image"]
        self.ipf_graph.add_connection(oport, iport)
        self.ipf_graph.process()
        self.ipf_graph.save("files/test.xml")
        self.assertTrue(filecmp.cmp("files/test.xml", "files/test_file_reference.xml"))
        
    
    def test_no_connection_process(self):
        self.ipf_graph.process()
        
        
    def test_save_and_load_all_blocks(self):
        block_classes = ipf.ipfgraphloader.get_ipfblock_classes()
        for block_name in block_classes:
            self._test_save_and_load_block( block_classes[block_name])
        
        
    def _test_save_and_load_block(self, block_class):
        graph = ipf.ipfgraph.IPFGraph()
        graph.add_block(block_class.__name__, block_class())
        graph.save("files/test_block.xml")
        new_graph = ipf.ipfgraphloader.load("files/test_block.xml")
        new_graph.save("files/test_block_load.xml")
        self.assertTrue(filecmp.cmp("files/test_block.xml", 
                                    "files/test_block_load.xml"))



if __name__ == "__main__":
    unittest.main()