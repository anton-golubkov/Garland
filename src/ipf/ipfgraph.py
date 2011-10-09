# -*- coding: utf-8 -*-

from pygraph.classes.digraph import digraph
from pygraph.algorithms.sorting import topological_sorting
import xml.etree.ElementTree
from xml.etree.ElementTree import Element 
from xml.etree.ElementTree import SubElement

from keyfromvalue import dict_key_from_value
import ipfblock
import ipfblock.connection

class IPFGraph(object):
    """ Image processing flow graph
    
        This class represents image processing chain. 
    """

    # Grid model constants 
    max_grid_width = 20
    max_grid_height = 200

    def __init__(self):
        self.blocks = dict() # {"Block name" : IPFBlock}
        self.connections = [] 
        self._grid_width = 5
        self._grid_height = 5
        
        # Create empty 2-dimension list for blocks in grid
        self._grid_model = [ [None for j in xrange(self.max_grid_width)] \
                             for i in xrange(self.max_grid_height) ]
    
    
    def add_block(self, block_name, ipf_block, row=-1, column=-1):
        self.blocks[block_name] = ipf_block
        if row >= 0 and column >= 0:
            # Add block to grid_model
            if not self.grid_cell_empty(row, column):
                # This cell is occupied 
                raise ValueError("Cell (%d, %d) already occupied" % \
                                 (row, column))
            
            if not self.cell_in_grid(row, column):
                raise ValueError("Wrong cell address: (%s, %s); grid size: (%s, %s)" % \
                              (column, row, self._grid_width, self._grid_height))
                
            self._grid_model[row][column] = ipf_block
            
            
    def remove_block(self, block_name):
        block = self.blocks[block_name]
        cell = self.get_block_cell(block)
        if cell is not None:
            row, column = cell
            self._grid_model[row][column] = None
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
            node.process()
    
    def get_block_name(self, block):
        return dict_key_from_value(self.blocks, block)
    
    
    def xml(self):
        """ Return IPFGraph as XML element
        
        """
        graph = Element("IPFGraph")
        block_tree = SubElement(graph, "Blocks")
        for name in self.blocks:
            block_element = SubElement(block_tree, "Block", {"name": name})
            block_element.append(self.blocks[name].xml())
        
        connection_tree = SubElement(graph, "Connections")
        for connection in self.connections:
            oport = connection._oport
            iport = connection._iport
            oblock = oport._owner_block
            iblock = iport._owner_block
            oblock_name = self.get_block_name(oblock)
            iblock_name = self.get_block_name(iblock)
            oport_name = oblock.get_port_name(oport)
            iport_name = iblock.get_port_name(iport)
            conection_element = SubElement(connection_tree, "Connection")
            con_output = SubElement(conection_element, 
                                   "ConnectionOutput",
                                   {"block" : oblock_name,
                                    "port" : oport_name})
            con_input = SubElement(conection_element, 
                                   "ConnectionInput",
                                   {"block" : iblock_name,
                                    "port" : iport_name})
        return graph
    
            
    def save(self, file_name):
        """ Save IPFGraph as XML file 
        
        """
        root = Element("Garland")
        root.attrib["Version"] = "1.0"
        root.append(self.xml())
        str_root = xml.etree.ElementTree.tostring(root, encoding='utf-8')
        with  open(file_name, "w") as file:
            file.write(str_root)
        
    
    def get_grid_size(self):
        return (self._grid_width, self._grid_height)
        
    
    def grid_cell_empty(self, row, column):
        return self._grid_model[row][column] is None
    
    
    def cell_in_grid(self, row, column):
        return row >= 0 and row < self._grid_height and \
               column >= 0 and column < self._grid_width
               
    
    def get_block_cell(self, block):
        for row in range(self._grid_height):
            for column in range(self._grid_width):
                if self._grid_model[row][column] == block:
                    return (row, column)
        return None
    
    def move_block(self, block, row, column):
        from_cell = self.get_block_cell(block)
        if from_cell is not None and self.grid_cell_empty(row, column):
            block_row, block_column = from_cell
            self._grid_model[block_row][block_column] = None
            self._grid_model[row][column] = block
        else:
            raise ValueError("Can`t move block to (%d, %d)" % \
                                 (row, column)) 
            
    def add_row(self):
        if self.max_grid_height > self._grid_height:
            self._grid_height += 1
        else:
            raise ValueError("Max row count reached")
        
    def add_column(self):
        if self.max_grid_width > self._grid_width:
            self._grid_width += 1
        else:
            raise ValueError("Max column count reached")