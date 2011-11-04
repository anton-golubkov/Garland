# -*- coding: utf-8 -*-

""" Factory classes for loading IPFGraph from xml file

"""

import pkgutil
import inspect
import os
from xml.etree.ElementTree import ElementTree

from ipfblock.ipfblock import IPFBlock
from ipfgraph import IPFGraph
from ipftype.ipftype import IPFType
from ipfblock.property import Property
from getblockclasses import get_ipfblock_classes
from getblockclasses import get_type_classes

    
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
    type_classes = get_type_classes()
    
    for block_node in blocks_node.getiterator("Block"):
        block_name = block_node.attrib["name"]
        block_class_node = list(block_node)[0]
        class_name = block_class_node.tag
        block = ipfblock_classes[class_name]()
        properties_node = block_class_node.find("Properties")
        
        # Add properties to block
        for property_node in properties_node.getiterator("Property"):
            property_name = property_node.attrib["name"]
            value_node = property_node.find("PropertyValue")
            property_type = value_node.attrib["data_type"]
            max_value = value_node.attrib["max_value"]
            if len(max_value) == 0:
                max_value = None
            else:
                # Convert limit value to property data type
                max_value = type_classes[property_type].convert(max_value)
            min_value = value_node.attrib["min_value"]
            if len(min_value) == 0:
                min_value = None
            else:
                # Convert limit value to property data type
                min_value = type_classes[property_type].convert(min_value)
            value = value_node.attrib["value"]
            property = Property(type_classes[property_type]())
            property.max_value = max_value
            property.min_value = min_value
            property.set_value(value)
            block.properties[property_name] = property
            
        # Add ports to block
        # !!! In this version we don`t load ports information 
        # because ports created in block constructor and can`t be deleted or created
        
        # Add block to graph
        graph.add_block(block_name, block) 
        
        
    # Load connections
    connections_node = ipfgraph_node.find("Connections")
    for connection_node in connections_node.getiterator("Connection"):
        con_output_node = connection_node.find("ConnectionOutput")
        oblock_name = con_output_node.attrib["block"]
        oblock_port = con_output_node.attrib["port"]
        oport = graph.__blocks[oblock_name].output_ports[oblock_port]
        con_input_node = connection_node.find("ConnectionInput")
        iblock_name = con_input_node.attrib["block"]
        iblock_port = con_input_node.attrib["port"]
        iport = graph.__blocks[iblock_name].input_ports[iblock_port]
        graph.add_connection(oport, iport)
        
    return graph
