# -*- coding: utf-8 -*-


class Property(object):
    """ Base IPFBlock property class
    
    """

    def __init__(self):
        self.type = None
        self.value = None
        self.min_value = None
        self.max_value = None
        