# -*- coding: utf-8 -*-

import ipfblock
import ioport
import ipf.ipfblock.processing
from property import Property
from ipf.ipftype.ipfimage1ctype import IPFImage1cType
from ipf.ipftype.ipfinttype import IPFIntType
from ipf.ipftype.ipfthresholdtype import IPFThresholdType
from ipf.ipfblock.threshold import Threshold

class ThresholdOtsu(Threshold):
    """ Threshold block
    
    """
    type = "ThresholdOtsu"
    category = "Filters"
    is_abstract_block = False
    
    def __init__(self):
        super(ThresholdOtsu, self).__init__()
        # Otsu`s threshold automatically calculate threshold value 
        del self.properties["threshold"]
        self.processing_function = ipf.ipfblock.processing.threshold_otsu

    def get_preview_image(self):
        return self.output_ports["output_image"]._value         
        
    
    

