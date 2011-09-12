# -*- coding: utf-8 -*-

import property

class RGBProperty(property.Property):
    """ RGB color IPFBlock property class
    
    """

    def __init__(self):
        self.type = "RGB"
        self.value = [0, 0, 0]
        self.min_value = [0, 0, 0]
        self.max_value = [255, 255, 255]
        