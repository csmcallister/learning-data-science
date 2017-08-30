from PIL import Image as pillow_image
import pytesseract
import argparse
import cv2
import os
import PyPDF2
import numpy as np
from matplotlib import pyplot as plt
%matplotlib inline
from wand.image import Image
# wand required: $ brew install imagemagick@6  (get version 6)
#                $ export MAGICK_HOME=/usr/local/opt/imagemagick@6
#                $ brew link imagemagick@6 --force
#                $ brew install ghostscript
import io

# import pdf and convert to image
with Image(filename="pdf-sample.pdf") as img:
     img.save(filename="test.jpg")

# load the example image and convert it to grayscale
image = cv2.imread('test.jpg')


#####################################################################
# (Optional) 2D Convolution ( Image Filtering ) to improve resolution
img = cv2.imread('test.jpg')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
#####################################################################
# write the grayscale image to disk as a temporary file so we can apply OCR to it
filename = "{}.jpg".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
text = pytesseract.image_to_string(pillow_image.open('test.jpg'))
os.remove(filename)
# print the text we've stored as a string
print(text)
