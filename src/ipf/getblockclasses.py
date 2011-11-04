# -*- coding: utf-8 -*-


import pkgutil
import inspect
import os

from ipfblock.ipfblock import IPFBlock
from ipftype.ipftype import IPFType


def get_classes_from_module(base_class, 
                            is_accepted=lambda x: True):
    """ Create dict {"class_name" : class object } for all classes
        based on given base_class
        is_accepted function checks if given class need to be added in dict
    """
    parent_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
    modules = [ cls for iter, cls, ispkg in \
                pkgutil.walk_packages([parent_folder,]) ]
    classes = dict()
    for module_name in modules:
        mod = __import__(module_name, fromlist = ["Whatever need for import"])
        for name, obj in inspect.getmembers(mod):
            if inspect.isclass(obj):
                # Don`t add base_class to dict
                if issubclass(obj, base_class) and obj != base_class:
                    if is_accepted(obj):
                        classes[name] = obj
    return classes 

def get_ipfblock_classes():
    """ Create dict {"block_name" : IPFBlock class } for all IPFBlock subclasses
    
        This dict will be used in file loading process
    """
    return get_classes_from_module(IPFBlock, lambda x: not x.is_abstract_block)
    
    
def get_type_classes():
    """ Create dict {"typename" : Type class } for all IPFType subclasses
    
        This dict will be used in file loading process
    """
    return get_classes_from_module(IPFType) 
