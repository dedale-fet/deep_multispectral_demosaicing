# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals

import numpy as np


from .mosaic_mask import get_mosaic_masks


def mosaicing_generic(image, patternSize=[3,3], channelOrder=np.arange(0,9)):
    """
    Returns the CFA mosaic for given *patternSize* and *channelOrder*.

    Parameters
    ----------
    image : array_like
        multichannel array

    patternSize : array_like
        shape of the macropixel [height, width]

    channelOrder : array_like
        Arrangement of the colour filters in a macropixel
        default : [0, 1, ..., 8], corresponding to the following pattern
           0 1 2
           3 4 5
           6 7 8

    Returns
    -------
    ndarray
        mosaic image.

    """
    
    image = np.asarray(image)

    masks = get_mosaic_masks(image.shape[0:2], patternSize, channelOrder)

    mosaic = np.zeros(image.shape[0:2])
    for c, mask in masks.items():
        mosaic = mosaic + image[:,:,c] * mask

    return mosaic
