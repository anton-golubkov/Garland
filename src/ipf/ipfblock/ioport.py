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

import xml.etree.ElementTree
from xml.etree.ElementTree import Element 
from xml.etree.ElementTree import SubElement
import weakref


class Port(object):
    """ Base IPFBlock port class
    
    """
    
    def __init__(self, ipfblock, data_type):
        """ Base port class constructor """
        if ipfblock is not None:
            self._owner_block = weakref.ref(ipfblock)
        self._data_type = data_type
        self._value = data_type.default_value()
        
    
    def _set_value(self, value):
        """ Protected function for use in IPFBlock
        
        """
        self._value = self._data_type.convert(value)
        
    def _get_value(self):
        return self._value
    
    def process(self):
        """ Empty function for using in IPFGraph 
        
            This function must be in all classes which stored in IPFGraph 
        """
        pass
    
    def xml(self):
        """ Return port object as XML element 
        
        """
        port_element = Element("Port")
        port_element.attrib["DataType"] = self._data_type.name
        #port_element.attrib["Value"] = self._value
        return port_element
        

class IPort(Port):
    """ Input port class for IPFBlock
    
    """
    
    def __init__(self, ipfblock, data_type):
        super(IPort, self).__init__(ipfblock, data_type)
        self._port_free = True
        
    def pass_value(self, value):
        """ Pass value to input port
        """
        self._value = self._data_type.convert(value)
        
    def is_free(self):
        return self._port_free
    
    def set_free(self):
        self._port_free = True
        
    def set_binded(self):
        self._port_free = False
        
    def invalidate(self):
        self._valid = False
        
    
    
class OPort(Port):
    """ Output port class for IPFBlock
    
    """
    
    def __init__(self, ipfblock, data_type):
        super(OPort, self).__init__(ipfblock, data_type)
        self._binded_count = 0
        
    def get_value(self):
        return self._value

    def is_free(self):
        return self._binded_count == 0
    
    def increase_binded_count(self):
        self._binded_count += 1
        
    def decrease_binded_count(self):
        if self._binded_count <= 0:
            raise ValueError("OPort error: _binded_count less than 1")
        else:
            self._binded_count -= 1
    

def compatible(port1, port2):
    """ Check ports types compatibility
    
        If output port type has similar properties as input port data type
        then ports assuming compatible.
    
    """
    # Both input or both output ports is not compatible
    if type(port1) == type (port2):
        return False
    
    # Find witch of ports is input and witch is output
    # 
    iport = None
    oport = None
    
    if type(port1) == IPort and type(port2) == OPort:
        iport = port1
        oport = port2
    elif type(port1) == OPort and type(port2) == IPort:
        iport = port2
        oport = port1
    else:
        return False
    
    return iport._data_type.is_compatible(oport._data_type)
    
        
def is_connect_allowed(port1, port2):
    """ Return True if ports can be connected, False otherwise
    
    """
    
    if not compatible(port1, port2):
        return False
    
    # Find witch of ports is input and witch is output
    # 
    iport = None
    
    if type(port1) == IPort:
        iport = port1
    elif type(port2) == IPort:
        iport = port2
    else:
        return False
    
    if iport.is_free():
        return True
    
    
    
    
