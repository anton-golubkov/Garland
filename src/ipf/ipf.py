# -*- coding: utf-8 -*-

from pygraph.classes.digraph import digraph
from pygraph.algorithms.sorting import topological_sorting

import ipfblock
import ipfblock.connection

class IPFGraph(object):
    """ Image processing flow graph
    
        This class represents image processing chain. 
    """

    def __init__(self):
        self.blocks = dict() # {"Block name" : IPFBlock}
        self.connections = [] 
        
    def add_block(self, block_name, ipf_block):
        self.blocks[block_name] = ipf_block
    
    def remove_block(self, block_name):
        del self.blocks[block_name]
    
    def add_connection(self, oport, iport):
        """ Add connection between input (iport) and output (oport) ports 
            
            Function raises exception ValueError if ports can`t be connected.
        """
        con = ipfblock.connection.Connection(oport, iport)
        self.connections.append(con)
        
    def process(self):
        """ Process image processing flow for IPFGraph """
        
        # Invalidate all input ports in blocks
        ((iport.invalidate() for iport in block.input_ports.values()) 
                             for block in self.blocks.values())
        
        # Map image processing flow to directed graph
        # apply topological sorting and execute processing blocks in
        # topological order 
        
        graph = digraph()
        for block in self.blocks:
            graph.add_node(self.blocks[block])
            for iport in self.blocks[block].input_ports.values():
                graph.add_node(iport)
                graph.add_edge( (iport, self.blocks[block]) )
            for oport in self.blocks[block].output_ports.values():
                graph.add_node(oport)
                graph.add_edge( (self.blocks[block], oport) )
        for connection in self.connections:
            graph.add_node(connection)
            graph.add_edge( (connection._oport, connection) )
            graph.add_edge( (connection, connection._iport) )
        
        sorted_graph = topological_sorting(graph)
        for node in sorted_graph:
            print node
        
    
    
        
        
        