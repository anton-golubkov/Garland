#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest


import os, sys
cmd_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


import ipf.ipf
import ipf.ipfblock.rgb2gray
import cv

class TestIPFGraph(unittest.TestCase):

    def setUp(self):
        self.ipf_graph = ipf.ipf.IPFGraph()
        block = ipf.ipfblock.rgb2gray.RGB2Gray()
        self.test_image = cv.LoadImage("test.png")
        self.block.input_ports["input_image"].pass_value(self.test_image)


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()