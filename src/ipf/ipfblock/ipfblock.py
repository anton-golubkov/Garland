# -*- coding: utf-8 -*-

import xml.etree.ElementTree
from xml.etree.ElementTree import Element 
from xml.etree.ElementTree import SubElement

from ipf.keyfromvalue import dict_key_from_value


class IPFBlock(object):
    """ Base image processing flow block class
    
    """
    # Class members
    type = "IPFBlock"
    category = ""
    
    # Tells that block is abstract and can not be created
    is_abstract_block = True
    
    # Block instanced number
    # Used for generation of unique block names
    block_number = 0
    
    def __init__(self):
        self.input_ports = dict() # {"name" : IPort object}
        self.output_ports = dict() # {"name" : OPort object}
        self.properties = dict() # {"name" : Property object}
        self.processing_function = None # Image processing function
        IPFBlock.block_number += 1
        
    def process(self):
        """ Execute IPFBlock process. Sets results to output ports values
        
            Input ports names binded to processing function named arguments
        
        """
        input = dict()
        for key in self.input_ports:
            input[key] = self.input_ports[key]._get_value()
        for key in self.properties:
            input[key] = self.properties[key].get_value() 
        if self.processing_function is not None:
            output = self.processing_function(input)
            for key in output:
                if self.output_ports.has_key(key) and output[key] is not None:
                    self.output_ports[key]._set_value(output[key])
                    
    def xml(self):
        """ Return block object in XML element 
        
        """
        block = Element(self.type)
        
        input_ports_tree = SubElement(block, "InputPorts")
        for port in self.input_ports:
            port_element = SubElement(input_ports_tree, "InputPort", {"name" : port})
            port_element.append(self.input_ports[port].xml())
        
        output_ports_tree = SubElement(block, "OutputPorts")
        for port in self.output_ports:
            port_element = SubElement(output_ports_tree, "OutputPort", {"name" : port})
            port_element.append(self.output_ports[port].xml())
        
        properties_tree = SubElement(block, "Properties")
        for property in self.properties:
            property_element = SubElement(properties_tree, "Property", {"name" : property})
            property_element.append(self.properties[property].xml())
            
        return block
    
    def get_port_name(self, port):
        iport_name = dict_key_from_value(self.input_ports, port)
        if iport_name is not None:
            return iport_name
        oport_name = dict_key_from_value(self.output_ports, port)
        return oport_name
    
    def get_preview_image(self):
        """ Return block processing result in form of image
        
            If no result is available, function returns None 
        """
        return None
            
        
        
    
    

