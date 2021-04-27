#imports
import sys
from PIL import Image, ImageDraw, ImageEnhance
import numpy as np
import cv2
import skimage
from scipy import ndimage as ndi
from skimage import feature, color,io
from skimage.morphology import square
import matplotlib.pyplot as plt
import math
from skimage.transform import probabilistic_hough_line
from builtins import input
import argparse

# Haning for shell script 
vari=sys.argv[1]
img = plt.imread(vari)
lab=str(vari).split('.')
lab=lab[0]+'_filt.jpg'

# normal analysis#

###Fist code block##
# Read in image and Choose color channel
img = plt.imread(vari)
img=img[:,:,2] # gets color channel 

# adjust contrast (these parameters can be palyed with) #gamma 3 to start
img = skimage.exposure.adjust_gamma(img, gamma=2, gain=1)

# Chnage to grayscale and show
gray = color.rgb2gray(img)
plt.imshow(img,cmap=plt.cm.gray)
plt.axis('off')
plt.savefig('test.jpg', bbox_inches='tight', pad_inches=0, dpi = 300) #loop 2 0.8 loop 1 1.5
plt.close()

####### second code block ######


img = plt.imread('test.jpg')
img=img[:,:,2] # get color channel

# adjust contrast

gray = color.rgb2gray(img)

from skimage.morphology import disk
from skimage.filters.rank import mean
loc_mean = mean(img, disk(5))
plt.imshow(loc_mean, vmin=0, vmax=255, cmap=plt.cm.gray)
plt.axis('off')
plt.savefig('test3.jpg', bbox_inches='tight', pad_inches=0, dpi = 300) #loop 2 0.8 loop 1 1.5
plt.close()
####### Code Block 3 #######
# Filter using meijering - loc mean
img = plt.imread('test3.jpg')
img = skimage.filters.meijering(img,black_ridges=True)

# Turn to gray
gray = color.rgb2gray(img)

# Threshold and turn to binary
threshold = skimage.filters.threshold_otsu(gray)
binary = (gray >= threshold)

# Filter noise -erosion filter
out = ndi.morphology.binary_erosion(binary, iterations=5)

# Show image
plt.imshow(out, cmap=plt.cm.gray)
plt.axis('off')
plt.savefig(lab, bbox_inches='tight', pad_inches=0, dpi = 300) #loop 2 0.8 loop 1 1.5
plt.close()