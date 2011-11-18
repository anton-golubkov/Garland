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

    
    def test_add_block(self):
        self.ipf_graph.add_block("ImageInput", "input_image")
        self.ipf_graph.add_block("RGB2Gray", "rgb2gray1")
        self.assertTrue(self.ipf_graph.get_block("input_image"))
        self.assertTrue(self.ipf_graph.get_block("rgb2gray1"))
        
    
    def test_remove_block(self):
        self.ipf_graph.add_block("ImageInput", "input_image")
        self.ipf_graph.add_block("RGB2Gray", "rgb2gray1")
        self.ipf_graph.remove_block("input_image")
        self.assertTrue(self.ipf_graph.get_block("input_image") is None)
        self.ipf_graph.remove_block("rgb2gray1")
        self.assertTrue(self.ipf_graph.get_block("rgb2gray1") is None)
    
    
    def test_add_connection(self):
        self.ipf_graph.add_block("ImageInput", "input_image")
        self.ipf_graph.add_block("RGB2Gray", "rgb2gray1")
        oport = self.ipf_graph.get_block("input_image").output_ports["output_image"]
        iport = self.ipf_graph.get_block("rgb2gray1").input_ports["input_image"]
        self.ipf_graph.add_connection(oport, iport)
        self.assertEqual(len(self.ipf_graph.connections), 1 )
        for connection in self.ipf_graph.connections:
            self.assertEqual(connection._oport(), oport)
            self.assertEqual(connection._iport(), iport)
    
    
    def test_delete_block_with_connections(self):
        self.ipf_graph.add_block("ImageInput", "input_image")
        self.ipf_graph.add_block("RGB2Gray", "rgb2gray1")
        oport = self.ipf_graph.get_block("input_image").output_ports["output_image"]
        iport = self.ipf_graph.get_block("rgb2gray1").input_ports["input_image"]
        self.ipf_graph.add_connection(oport, iport)
        self.ipf_graph.remove_block("input_image")
        self.assertEqual(len(self.ipf_graph.connections), 0 )
        
    
    def test_process(self):
        self.ipf_graph.add_block("ImageInput", "input_image")
        self.ipf_graph.get_block("input_image").properties["file_name"].set_value("files/test.png")
        self.ipf_graph.add_block("RGB2Gray", "rgb2gray1")
        oport = self.ipf_graph.get_block("input_image").output_ports["output_image"]
        iport = self.ipf_graph.get_block("rgb2gray1").input_ports["input_image"]
        self.ipf_graph.add_connection(oport, iport)
        self.ipf_graph.process()
        # This flow must return gray image
        test_image = cv.LoadImage("files/test.png")
        gray_image = cv.CreateImage(cv.GetSize(test_image), cv.IPL_DEPTH_8U, 1)
        cv.CvtColor(test_image, gray_image, cv.CV_RGB2GRAY)
        processed_image = self.ipf_graph.get_block("rgb2gray1").output_ports["output_image"].get_value() 
        self.assertEqual(processed_image.tostring(), gray_image.tostring())
        
    
    def test_save(self):
        self.ipf_graph.add_block("ImageInput", "input_image")
        self.ipf_graph.get_block("input_image").properties["file_name"].set_value("files/test.png")
        self.ipf_graph.add_block("RGB2Gray", "rgb2gray1")
        oport = self.ipf_graph.get_block("input_image").output_ports["output_image"]
        iport = self.ipf_graph.get_block("rgb2gray1").input_ports["input_image"]
        self.ipf_graph.add_connection(oport, iport)
        self.ipf_graph.process()
        self.ipf_graph.save("files/test.xml")
        self.assertTrue(filecmp.cmp("files/test.xml", "files/test_file_reference.xml"))
        
    
    def test_no_connection_process(self):
        self.ipf_graph.process()
        
        
    def test_save_and_load_all_blocks(self):
        block_classes = ipf.ipfgraphloader.get_ipfblock_classes()
        for block_class_name in block_classes:
            self.help_test_save_and_load_block( block_class_name)
        
        
    def help_test_save_and_load_block(self, block_class_name):
        graph = ipf.ipfgraph.IPFGraph()
        graph.add_block(block_class_name, block_class_name)
        graph.save("files/test_block.xml")
        new_graph = ipf.ipfgraphloader.load("files/test_block.xml")
        new_graph.save("files/test_block_load.xml")
        self.assertTrue(filecmp.cmp("files/test_block.xml", 
                                    "files/test_block_load.xml"))
        
        
    def test_add_block_to_grid(self):
        self.assertTrue(self.ipf_graph.grid_cell_empty(1, 1))
        self.ipf_graph.add_block("ImageInput", "input_image", 1, 1)
        self.assertTrue(self.ipf_graph.get_block("input_image"))
        self.assertFalse(self.ipf_graph.grid_cell_empty(1, 1))
        
        self.assertTrue(self.ipf_graph.grid_cell_empty(2, 2))
        self.ipf_graph.add_block("RGB2Gray", "rgb2gray1", 2, 2)
        self.assertTrue(self.ipf_graph.get_block("rgb2gray1"))
        self.assertFalse(self.ipf_graph.grid_cell_empty(2, 2))
        
        
    def test_delete_block_from_grid(self):
        self.ipf_graph.add_block("ImageInput", "input_image", 1, 1)
        self.ipf_graph.add_block("RGB2Gray", "rgb2gray1", 2, 2)
        
        self.ipf_graph.remove_block("input_image")
        self.assertFalse(self.ipf_graph.get_block("input_image"))
        
        self.ipf_graph.remove_block("rgb2gray1")
        self.assertTrue(self.ipf_graph.get_block("rgb2gray1") is None)
        
        
        self.assertTrue(self.ipf_graph.get_block_cell("input_image") is None)
        self.assertTrue(self.ipf_graph.get_block_cell("rgb2gray1") is None)
        self.assertTrue(self.ipf_graph.grid_cell_empty(1, 1))
        self.assertTrue(self.ipf_graph.grid_cell_empty(2, 2))


    def test_add_unknown_block(self):
        self.assertRaises(
            ValueError,
            self.ipf_graph.add_block,
            "UnknownBlockClass", 
            "block")
        
    def test_add_block_without_name(self):
        block_ref = self.ipf_graph.add_block("ImageInput", None, 1, 1)
        self.assertTrue(block_ref() is not None)
        block_name = self.ipf_graph.get_block_name(block_ref())
        self.assertTrue(len(block_name) > 0)
        block_ref2 = self.ipf_graph.add_block("ImageInput", None, 2, 2)
        self.assertTrue(block_ref2() is not None)
        block_name2 = self.ipf_graph.get_block_name(block_ref2())
        self.assertTrue(len(block_name2) > 0)
        self.assertTrue (block_name != block_name2)
        
        
    def test_add_blocks_to_same_cell(self):
        self.ipf_graph.add_block("ImageInput", "input_image1", 1, 1)
        self.assertRaises(
            ValueError,
            self.ipf_graph.add_block,
            "ImageInput", 
            "input_image2",
            1,
            1)
    
    
    def test_add_block_with_same_name(self):
        self.ipf_graph.add_block("ImageInput", "input_image1")
        self.assertRaises(
            ValueError,
            self.ipf_graph.add_block,
            "ImageInput", 
            "input_image1")
        
        
    def test_is_accessible(self):
        self.ipf_graph.add_block("Dilate", "block1")
        self.ipf_graph.add_block("Dilate", "block2")
        block1 = self.ipf_graph.get_block("block1")
        block2 = self.ipf_graph.get_block("block2")
        iport1 = self.ipf_graph.get_block("block1").input_ports["input_image"]
        oport1 = self.ipf_graph.get_block("block1").output_ports["output_image"]
        iport2 = self.ipf_graph.get_block("block2").input_ports["input_image"]
        oport2 = self.ipf_graph.get_block("block2").output_ports["output_image"]
        self.ipf_graph.add_connection(oport1, iport2)
        self.assertTrue(self.ipf_graph.is_accessible(oport1, iport2))
        self.assertFalse(self.ipf_graph.is_accessible(iport2, oport1))
        self.assertTrue(self.ipf_graph.is_accessible(iport1, oport2))
        self.assertTrue(self.ipf_graph.is_accessible(iport1, iport2))
        self.assertTrue(self.ipf_graph.is_accessible(block1, block2))
        self.assertFalse(self.ipf_graph.is_accessible(block2, block1))
        
        
        
        
        


if __name__ == "__main__":
    unittest.main()
    
    