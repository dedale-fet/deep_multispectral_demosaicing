# -*- coding: utf-8 -*-

import spectral as SPy


def readMultispectralImage(imagePath, nBits=16, withMetadata=False):
    hdr_path = imagePath[:-4] + '.hdr'
    imagePointer = SPy.open_image(hdr_path)
    image = imagePointer[:, :, :].squeeze()
    image = image.astype('float') / (2 ** nBits - 1)
    if withMetadata:
        return image, imagePointer.metadata
    else:
        return image

def writeMultispectralImage(savingPath, image, numBits=8, metadata=[]):
    if numBits > 8:
        image = image.astype('uint16')
    else:
        image = image.astype('uint8')
    hdr_path = savingPath[:-4]+'.hdr'
    SPy.envi.save_image(hdr_path, image, force=True, metadata = metadata)
