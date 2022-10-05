#TODO: add functionality to add different style where mask is
#TODO: clean up code and use functions to make code easy to use and extend

import numpy as np
import cv2

def apply_mask(mask_path, transfered_path, overlay_img_path):
    mask_img, transfered_img, overlay_img = read_imgs_from_paths(mask_path, transfered_path, overlay_img_path)
    shape = transfered_img.shape
    mask_img, overlay_img = resize_imgs(mask_img, overlay_img, shape)
    binarization(mask_img)
    result_img = mask_overlay(overlay_img, transfered_img, mask_img)
    return result_img


def read_imgs_from_paths(mask_path, transfered_path, overlay_img_path):
    transfered_img = cv2.imread(transfered_path, 1) #color image
    overlay_img = cv2.imread(overlay_img_path, 1) #color image
    mask_img = cv2.imread(mask_path, 0) # grayscale mask load
    return mask_img, transfered_img, overlay_img


def resize_imgs(mask_img, overlay_img, shape):
    width, height, _ = shape
    mask_img = cv2.resize(mask_img, (height, width))
    overlay_img = cv2.resize(overlay_img, (height, width))
    return mask_img, overlay_img


# util function to load masks
def binarization(mask_img):
    mask_img[mask_img <= 127] = 0
    mask_img[mask_img > 128] = 255


# util function to apply mask to generated image
def mask_overlay(overlay_img, transfered_img, mask_img):
    width, height, _ = transfered_img.shape
    for i in range(width):
        for j in range(height):
            if mask_img[i, j] == 255:
                transfered_img[i, j, :] = overlay_img[i, j, :]

    return transfered_img


mask_path = "c:/Nico/Natangwe Arts/keras-io/code/images/nora_snow_mask.jpg"
generated_path = "c:/Nico/Natangwe Arts/keras-io/code/images/nora_snow_style1.jpg"
overlay_path = "c:/Nico/Natangwe Arts/keras-io/code/images/nora_snow_style2.jpg"

result = apply_mask(mask_path,generated_path, overlay_path)
cv2.imshow("mask", result)
cv2.waitKey(0)
cv2.destroyAllWindows()