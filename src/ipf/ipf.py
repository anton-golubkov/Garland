# -*- coding: utf-8 -*-


class IPFGraph(object):
    """ Image processing flow graph
    
        This class represents image processing chain. 
    """

    def __init__(self):
        self.blocks = dict() # {"Block name" : IPFBlock}
        self.connections = dict() 
        
    def add_block(self, ipf_block):
        pass
    
    def remove_block(self, ipf_block):
        pass
    
    def add_connection(self, oport, iport):
        """ Add connection between input (iport) and output (oport) ports 
            
            Function return IPFConnection object if ports can be connected
            or raises exception IPFConnectionError if ports can`t be connected.
        """
        pass