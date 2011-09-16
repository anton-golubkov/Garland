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
        