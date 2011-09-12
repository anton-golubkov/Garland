# -*- coding: utf-8 -*-

import property

class IntProperty(property.Property):
    """ Integer IPFBlock property class
    
    """

    def __init__(self):
        self.type = "Int"
        self.value = 0
        self.min_value = None
        self.max_value = None
        