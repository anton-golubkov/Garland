# -*- coding: utf-8 -*-

import property

class StringProperty(property.Property):
    """ String IPFBlock property class
    
    """

    def __init__(self):
        self.type = "String"
        self.value = ""
        self.min_value = None
        self.max_value = None
        