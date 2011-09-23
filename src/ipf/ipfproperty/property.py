# -*- coding: utf-8 -*-

import xml.etree.ElementTree
from xml.etree.ElementTree import Element 
from xml.etree.ElementTree import SubElement

class Property(object):
    """ Base IPFBlock property class
    
    """

    def __init__(self, data_type):
        self._data_type = data_type 
        self.value = data_type.default_value()
        self.min_value = None
        self.max_value = None
        
    def set_value(self, value):
        """ Set value to property (use data_type.convert() function)
        
        """
        self.value = self._data_type.convert(value)
    

    def xml(self):
        """ Return property object in XML element 
        
        """
        property_element = Element("PropertyValue")
        property_element.attrib["data_type"] = self._data_type.name
        if self.value is not None:
            property_element.attrib["value"] = str(self.value)
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
    