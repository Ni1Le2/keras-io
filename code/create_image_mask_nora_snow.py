# https://www.digitalocean.com/community/tutorials/arithmetic-bitwise-and-masking-python-opencv

import numpy as np
import cv2
import os


image_path = "c:/Nico/Natangwe Arts/keras-io/code/images/nora_snow.jpg"
print(image_path)
image = cv2.imread(image_path)
height, width, _ = image.shape
new_shape = int(width/2),int(height/2)
image = cv2.resize(image, new_shape)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_thresh = np.array([0,0,0])
upper_thresh = np.array([60,255,255])

# Threshold the HSV image
mask = cv2.inRange(hsv, lower_thresh, upper_thresh)

cv2.imshow("test", hsv)
cv2.waitKey(0)
cv2.imshow("test", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

imagename = "code/images/nora_snow_mask.jpg"
cv2.imwrite(imagename, mask)

