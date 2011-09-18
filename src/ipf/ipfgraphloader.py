# -*- coding: utf-8 -*-

""" Factory classes for loading IPFGraph from xml file

"""

import pkgutil
import inspect
import os
from xml.etree.ElementTree import ElementTree

from ipfblock.ipfblock import IPFBlock
from ipf import IPFGraph
from ipfproperty.property import Property


def get_classes_from_module(base_class):
    """ Create dict {"class_name" : class object } for all classes
        based on given base_class
    """
    parent_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
    modules = [ cls for iter, cls, ispkg in \
                pkgutil.walk_packages([parent_folder,]) ]
    classes = dict()
    for module_name in modules:
        mod = __import__(module_name, fromlist = ["Whatever need for import"])
        for name, obj in inspect.getmembers(mod):
            if inspect.isclass(obj):
                if issubclass(obj, base_class):
                    classes[name] = obj
    return classes 

def get_ipfblock_classes():
    """ Create dict {"block_name" : IPFBlock class } for all IPFBlock subclasses
    
        This dict will be used in file loading process
    """
    return get_classes_from_module(IPFBlock)
    
    
def get_property_classes():
    """ Create dict {"property_type" : Property class } for all Property subclasses
    
        This dict will be used in file loading process
    """
    return get_classes_from_module(Property) 


    
def load(file):
    tree = ElementTree()
    tree.parse(file)
    
    # Load blocks
    ipfgraph_node = tree.find("IPFGraph")
    if ipfgraph_node is None:
        return None
    
    graph = IPFGraph()
           
    blocks_node = ipfgraph_node.find("Blocks")
    
    if blocks_node is None:
        return graph
    
    ipfblock_classes = get_ipfblock_classes()
    property_classes = get_property_classes()
    
    for block_node in blocks_node.getiterator("Block"):
        block_class_node = list(block_node)[0]
        class_name = block_class_node.tag
        print class_name
        block = ipfblock_classes[class_name]()
        properties_node = block_class_node.find("Properties")
        for property_node in properties_node.getiterator("Property"):
            value_node = list(property_node)[0]
            property_type = value_node.tag
            print property_type 
            
            
    
    # Load connections
    connections_node = ipfgraph_node.find("Connections")
    for connection in connections_node.getiterator("Connection"):
        print connection
        
    
