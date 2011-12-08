#-------------------------------------------------------------------------------
# Copyright (c) 2011 Anton Golubkov.
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the GNU Public License v2.0
# which accompanies this distribution, and is available at
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
# 
# Contributors:
#     Anton Golubkov - initial API and implementation
#-------------------------------------------------------------------------------
#!/usr/bin/python
# -*- coding: utf-8 -*-

from PySide import QtGui, QtCore
import cv
import PIL.Image
import StringIO

def pilimage_to_iplimage(pil_image):
    # Check zero size of image 
    if pil_image.size == (0, 0):
        return cv.CreateImage( (0, 0), cv.IPL_DEPTH_8U, 3) 
    ipl_image = cv.CreateImageHeader(pil_image.size, cv.IPL_DEPTH_8U, 3)
    # The image rotation and reversion of the string is to swap RGB into BGR, 
    # that is used in OpenCV video encoding.
    cv.SetData(ipl_image, pil_image.rotate(180).tostring()[::-1])
    return ipl_image


def pilimage_to_qimage(pil_image):
    # Check zero size of image
    if pil_image.size == (0, 0):
        return QtGui.QImage()
    
    # There is something strange bug appears,
    # when returning QImage created from PIL data
    # This function changed to buffer IO operations
    strio = StringIO.StringIO()
    pil_image.save(strio, "PNG")
    strio.seek(0)
    image = QtGui.QImage()
    image.loadFromData(strio.read())
    return image


def iplimage_to_pilimage(ipl_image):
        """Converts an ipl_image into a PIL.Image
        
        This function may be obsolete. Use ipl_image.as_pil_image() instead.
        """
        # Check zero size of image
        if cv.GetSize(ipl_image) == (0, 0):
            return PIL.Image.Image()

        # Check 1-channel input image and convert it to 3-channel
        if( ipl_image.nChannels == 1):
            image3c = cv.CreateImage(cv.GetSize(ipl_image), cv.IPL_DEPTH_8U, 3)
            cv.Merge(ipl_image, ipl_image, ipl_image, None, image3c)
            ipl_image = image3c
            
        size = cv.GetSize(ipl_image)
        data = ipl_image.tostring()
        im_pil = PIL.Image.fromstring(
                    "RGB", size, data,
                    'raw', "BGR")
        return im_pil


def iplimage_to_qimage( ipl_image):
    pil_image = iplimage_to_pilimage(ipl_image)
    qimage = pilimage_to_qimage(pil_image)
    return qimage



def qimage_to_iplimage( qimage):
    pil_image = qimage_to_pilimage(qimage)
    ipl_image = pilimage_to_iplimage(pil_image)
    return ipl_image

    
def qimage_to_pilimage(qimage):
    # Check zero size of image
    if (qimage.width(), qimage.height()) == (0, 0):
        return PIL.Image.Image()
     
    ba = QtCore.QByteArray()
    buffer = QtCore.QBuffer(ba)
    buffer.open(QtCore.QIODevice.WriteOnly)
    qimage.save( buffer, "PNG" )
    strio = StringIO.StringIO()
    strio.write(buffer.data())
    buffer.close()
    strio.seek(0)
    pil_image = PIL.Image.open(strio)
    return pil_image


