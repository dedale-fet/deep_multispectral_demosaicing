# Deep Multispectral Demosaicing Demo

This is the source code implementation of demosaicinb multispectral images with 3x3 macropixels using deep learning. 

___

Files:

  * demo_multispectral_demosaicing.ipynb - Demonstration of demosaicing on a real full-multispectral image. 
  * data/ - contains an original image and the network
  * data/MSI_deep_3x3_demosaicing.onnx - Deep-learning model in an universal format to compute the demosaicing. 
  * data/multispectral_image_9bands.img, and .hdr - The multispectral test image, with 9 bands from visible to near infrared. 
    * Due to the size of the data, please download it from our google drive : 
    * https://drive.google.com/open?id=1VbCtaUg3rizanQwNI49FP3pgQq5-BoPc
    * https://drive.google.com/open?id=157qMwBJUIIRWxauQ9jIWuM6exeMmYznT
___

The network model used is inspired from [VDSR].
The network is trained on the public datasets from Tokyotech and on the CAVE MSI dataset, projected onto a 9-bands camera.

To run demo_multispectral_demosaicing.ipynb, you need to have Python, Caffe2, and the spectral package installed. 
