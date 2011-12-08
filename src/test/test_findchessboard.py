#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import cv

import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipfblock.findchessboard

class TestFindChessboardBlock(unittest.TestCase):
    def setUp(self):
        self.block = ipf.ipfblock.findchessboard.FindChessboard()
        
        
    def test_zero_image(self):
        zero_image = cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 1)
        self.block.input_ports["input_image"].pass_value(zero_image)
        self.block.process()
        output_array = self.block.output_ports["output_array"].get_value()
        self.assertTrue(output_array ==  [])
        
    
    def test_no_chessboard(self):
        self.test_image_no_chessboard = cv.LoadImage("files/test.png", 1)
        self.block.input_ports["input_image"].pass_value(self.test_image_no_chessboard)
        self.block.process()
        output_array = self.block.output_ports["output_array"].get_value()
        self.assertTrue(output_array ==  [])
        
    
    def test_find_chessboard(self):
        self.test_image_with_chessboard = cv.LoadImage("files/chess.jpg", 1)
        self.block.input_ports["input_image"].pass_value(self.test_image_with_chessboard)
        self.block.properties["width"].set_value(5)
        self.block.properties["height"].set_value(3)
        self.block.process()
        output_array = self.block.output_ports["output_array"].get_value()
        self.assertTrue(len(output_array) == 15)
        
    
    def test_find_chessboard_rotated(self):
        self.test_image_with_chessboard = cv.LoadImage("files/chess.jpg", 1)
        self.block.input_ports["input_image"].pass_value(self.test_image_with_chessboard)
        self.block.properties["width"].set_value(3)
        self.block.properties["height"].set_value(5)
        self.block.process()
        output_array = self.block.output_ports["output_array"].get_value()
        self.assertTrue(len(output_array) == 15)
        
        
    def test_not_find_chessboard_other_size(self):
        self.test_image_with_chessboard = cv.LoadImage("files/chess.jpg", 1)
        self.block.input_ports["input_image"].pass_value(self.test_image_with_chessboard)
        self.block.properties["width"].set_value(3)
        self.block.properties["height"].set_value(4)
        self.block.process()
        output_array = self.block.output_ports["output_array"].get_value()
        self.assertTrue(output_array == [])
        
        


if __name__ == '__main__':
    unittest.main()
    

