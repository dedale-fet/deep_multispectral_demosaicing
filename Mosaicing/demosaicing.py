# -*- coding: utf-8 -*-


import numpy as np
from scipy.signal import convolve2d
from .mosaic_mask import get_mosaic_masks

def demosaicing_generic_bilinear(bayerImage, patternSize=[3,3], channelOrder=np.arange(0,9)):
    bayerImage = np.asarray(bayerImage)
    masks = get_mosaic_masks(bayerImage.shape, patternSize, channelOrder)

    f = np.ones((1,patternSize[0]))
    f = convolve2d(f,f)
    f2 = convolve2d(f,f.transpose())
    f2 = f2 / np.sum(f)

    multichannelImage = np.zeros( tuple(list(bayerImage.shape)+[np.array(channelOrder).size]) ) 
    for c, mask in masks.items():
        multichannelImage[:,:,c] = convolve2d(bayerImage*mask, f2, 'same')
    
    return multichannelImage


