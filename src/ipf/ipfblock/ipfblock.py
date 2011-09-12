# -*- coding: utf-8 -*-

class IPFBlock(object):
    """ Base image processing flow block class
    
    """
    
    def __init__(self):
        self.input_ports = dict()   # {"name" : IPort object}
        self.output_ports = dict()  # {"name" : OPort object}
        self.type = "IPFBlock"
        self.properties = dict()    # {"name" : Property object}
        self.python_code = u""      # Python code of image processing
        self.python_function = u""  # Name of python function
        self.c_code = u""           # C code of image processing
        self.c_function = u""       # Name of C function
        
    
    

