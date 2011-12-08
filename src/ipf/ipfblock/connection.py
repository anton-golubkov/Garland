#-------------------------------------------------------------------------------
# Copyright (c) 2011 Anton Golubkov.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Lesser Public License v2.1
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     Anton Golubkov - initial API and implementation
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import ioport
import weakref

class Connection(object):
    """ Connection class for IPFBlock
    
        Connection binding OPort and IPort of some IPFBlocks 
    """


    def __init__(self, oport, iport):
        # Check port compatibility and free of input port
        if ioport.is_connect_allowed(oport, iport):
            self._oport = weakref.ref(oport)
            self._iport = weakref.ref(iport)
            self._oport().increase_binded_count()
            self._iport().set_binded()
        else:
            raise ValueError("Can not create Connection with given ports")
            
    def __del__(self):
        if self._oport() is not None:
            self._oport().decrease_binded_count()
        if self._iport() is not None:
            self._iport().set_free()
        
        
    def contains_port(self, port):
        return self._iport() == port or self._oport() == port
        
        
    def process(self):
        """ Send value from output port to input port """
        self._iport().pass_value(self._oport().get_value())
        
        
