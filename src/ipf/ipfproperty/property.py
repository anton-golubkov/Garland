# -*- coding: utf-8 -*-

import xml.etree.ElementTree
from xml.etree.ElementTree import Element 
from xml.etree.ElementTree import SubElement

class Property(object):
    """ Base IPFBlock property class
    
    """

    def __init__(self):
        self.type = None
        self.value = None
        self.min_value = None
        self.max_value = None

    def xml(self):
        """ Return property object in XML element 
        
        """
        property_element = Element(self.type)
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
    