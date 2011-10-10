# -*- coding: utf-8 -*-

import xml.etree.ElementTree
from xml.etree.ElementTree import Element 
from xml.etree.ElementTree import SubElement

class Property(object):
    """ Base IPFBlock property class
    
    """

    def __init__(self, data_type, min_value=None, max_value=None):
        self._data_type = data_type 
        self._value = data_type.default_value()
        self.min_value = min_value
        self.max_value = max_value
        # If min_value is given set it as init value
        if min_value is not None:
            self._value = min_value
        
        
    def set_value(self, value):
        """ Set value to property (use data_type.convert() function)
        
        """
        new_value = self._data_type.convert(value)
        
        # Test value limits
        if (self.min_value is not None and new_value < self.min_value) or \
           (self.max_value is not None and new_value > self.max_value): 
            raise ValueError("Value %s outside property limits (%s, %s)" %\
                             (new_value, self.min_value, self.max_value))

        self._value = self._data_type.convert(value)
        
    
    
    def get_value(self):
        """ Get value of property
        
        """
        
        return self._value 
    
    
    def get_value_representation(self):
        """ Get view of value
        
            Function using for Dictionary data types, witch have name and data
            for values
        
        """
        
        return self._data_type.get_value_representation(self._value)
    
    
    def get_value_list(self):
        """ Return list of all possible values
        
            Function used for Dictionary data types
        """
        
        return self._data_type.get_value_list()
    

    def xml(self):
        """ Return property object in XML element 
        
        """
        property_element = Element("PropertyValue")
        property_element.attrib["data_type"] = self._data_type.name
        if self._value is not None:
            property_element.attrib["value"] = str(self.get_value_representation())
        else:
            property_element.attrib["value"] = ""
        if self.min_value is not None:
            property_element.attrib["min_value"] = str(self.min_value)
        else:
            property_element.attrib["min_value"] = ""
        if self.max_value is not None:
            property_element.attrib["max_value"] = str(self.max_value)
        else:
            property_element.attrib["max_value"] = ""
        return property_element
    
    
    def get_data_type(self):
        return self._data_type
    