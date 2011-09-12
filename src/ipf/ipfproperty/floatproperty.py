# -*- coding: utf-8 -*-

import property

class FloatProperty(property.Property):
    """ Float IPFBlock property class
    
    """

    def __init__(self):
        self.type = "Float"
        self.value = 0.0
        self.min_value = None
        self.max_value = None
        