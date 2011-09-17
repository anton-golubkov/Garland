# -*- coding: utf-8 -*-

""" Factory classes for loading IPFGraph from xml file

"""

import pkgutil
import inspect
import os

from ipfblock.ipfblock import IPFBlock

def get_ipfblock_classes():
    """ Create dict {"block_name" : IPFBlock class } for all IPFBlock subclasses
    
        This dict will be used in file loading process
    """
    parent_folder, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))
    block_modules = [ cls for iter, cls, ispkg in \
                      pkgutil.walk_packages([parent_folder,]) \
                      if cls.startswith("ipf.ipfblock.") ]
    block_classes = dict()
    for module_name in block_modules:
        mod = __import__(module_name, fromlist = ['Whatever need for import'])
        for name, obj in inspect.getmembers(mod):
            if inspect.isclass(obj):
                if issubclass(obj, IPFBlock):
                    block_classes[name] = obj
    return block_classes
      

    
    
