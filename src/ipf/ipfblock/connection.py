# -*- coding: utf-8 -*-

import ioport

class Connection(object):
    """ Connection class for IPFBlock
    
        Connection binding OPort and IPort of some IPFBlocks 
    """


    def __init__(self, oport, iport):
        # Check port compatibility and free of input port
        if ioport.is_connect_allowed(oport, iport):
            self._oport = oport
            self._iport = iport
            self._oport.increase_binded_count()
            self._iport.set_binded()
        else:
            raise ValueError("Can not create Connection with given ports")
            
    def __del__(self):
        self._oport.decrease_binded_count()
        self._iport.set_free()
        
    def process(self):
        """ Send value from output port to input port """
        self._iport.pass_value(self._oport.get_value())
        
        