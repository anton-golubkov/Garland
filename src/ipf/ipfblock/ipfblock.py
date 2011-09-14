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
        self.processing_function = None # Image processing function
        self.c_code = u""           # C code of image processing
        self.c_function = u""       # Name of C function
        
    def execute(self):
        """ Execute IPFBlock process. Sets results to output ports values
        
            Input ports names binded to processing function named arguments
        
        """
        input = dict()
        for key in self.input_ports:
            input[key] = self.input_ports[key]._get_value()
        if self.processing_function is not None:
            output = self.processing_function(input)
            for key in output:
                if self.output_ports.has_key(key):
                    self.output_ports[key]._set_value(output[key])
            
        
        
    
    

