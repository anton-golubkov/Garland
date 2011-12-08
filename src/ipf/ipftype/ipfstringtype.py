#-------------------------------------------------------------------------------
# Copyright (c) 2011 Anton Golubkov.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Lesser Public License v2.1
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     Anton Golubkov - initial API and implementation
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import ipftype

class IPFStringType(ipftype.IPFType):
    """ String data type class for use in image processing flow
    
    """

    name = "IPFStringType"
    this_type = type( "" )
        
    def __init__(self):
        pass
    
    @classmethod
    def default_value(cls):
        """ Return default value for this type """
        return ""        
    
    @classmethod
    def is_numeric(cls):
        return False
    
    @classmethod
    def is_image(cls):
        return False
    
    @classmethod
    def channel_count(cls):
        return 0
    
    @classmethod
    def is_array(cls):
        return True
    
        
