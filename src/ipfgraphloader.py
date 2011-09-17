# -*- coding: utf-8 -*-

""" Factory classes for loading IPFGraph from xml file

"""

import pkgutil
import inspect

import ipf.ipfblock.ipfblock

def load_ipfblock_modules():
    """ Create dict {"block_name" : IPFBlock class } for all IPFBlock subclasses
    
        This dict will be used in file loading process
    """
    block_modules = [ cls for iter, cls, ispkg in \
                      pkgutil.walk_packages("ipf.ipfblock") \
                      if cls.startswith("ipf.ipfblock.") ]
    for module_name in block_modules:
        print module_name
        mod = __import__(module_name, fromlist = ['Whatever need for import'])
        for name, obj in inspect.getmembers(mod):
            if inspect.isclass(obj):
                if issubclass(obj, ipf.ipfblock.ipfblock.IPFBlock):
                    print (name, obj)
    
        
        
        
if __name__ == "__main__":
    load_ipfblock_modules() 
    
    