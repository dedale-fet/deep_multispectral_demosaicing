# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals

import numpy as np


def get_mosaic_masks(shape, patternSize=[3,3], channelOrder=np.arange(0,9)):
    patternList = []
    for i in np.arange(0,patternSize[0]):
        for j in np.arange(0,patternSize[1]):
            patternList.append((i,j))
    channels = dict((channel, np.zeros(shape)) for channel in channelOrder)
    for channel, (i, j) in zip(channelOrder, patternList):
        channels[channel][i::patternSize[0], j::patternSize[1]] = 1
        channels[channel] = channels[channel].astype(bool)
    return channels

