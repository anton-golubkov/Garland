# -*- coding: utf-8 -*-

""" Functions for receive icons for blocks and ports   


"""

from PySide import QtGui

__type_icons = {"IPFImage3cType" : "icons/picture.png",
                "IPFImage1cType" : "icons/picture_gray.png",
                "IPFRGBType" : "icons/rgb.png",
                "IPFStringType" : "icons/text.png",
                "IPFIntType" : "icons/integer.png",
                "IPFFloatType" : "icons/integer.png",
                "IPFArrayType" : "icons/array.png",
                
                }


def get_image_for_type(type_name):
    global __type_icons
    if type_name not in __type_icons:
        return QtGui.QImage() 
    image = QtGui.QImage()
    image.load(__type_icons[type_name])
    return image

