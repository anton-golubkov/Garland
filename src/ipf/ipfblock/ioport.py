# -*- coding: utf-8 -*-


class Port(object):
    """ Base IPFBlock port class
    
    """
    
    def __init__(self, ipfblock, data_type):
        """ Base port class constructor """
        self._owner_block = ipfblock
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
        

class IPort(Port):
    """ Input port class for IPFBlock
    
    """
    
    def __init__(self, ipfblock, data_type):
        super(IPort, self).__init__(ipfblock, data_type)
        self._port_free = True
        self._valid = False # Indicate valid state of port value
        
    def pass_value(self, value):
        """ Pass value to input port
        """
        self._value = self._data_type.convert(value)
        self._valid = True
        
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
    

def compatible(oport, iport):
    """ Check ports types compatibility
    
        If output port type has similar properties as input port data type
        then ports assuming compatible.
    
    """
    return oport._data_type.is_compatible(iport._data_type)
    
        
