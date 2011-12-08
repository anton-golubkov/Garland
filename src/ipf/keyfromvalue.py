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
""" Return dict key by value

"""

def dict_key_from_value(dic, val):
        """ Return the key of dictionary dic given the value
        
        """
        values = [k for k, v in dic.iteritems() if v == val]
        if len(values) > 0:
            return values[0]
        else:
            return None
        
