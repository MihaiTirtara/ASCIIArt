from PIL import Image
import numpy as np
im = Image.open("ascii-pineapple.jpg")
ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def get_pixelMatrix(img) :
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0,len(pixels),img.width)]


def get_brightnessMatrix(matrix):
    new_matrix = []
    for x in range(len(matrix)):
        result = [sum(y)/ len(y) for y in matrix[x]]
    new_matrix.append(result)
    return new_matrix

pixels = get_pixelMatrix(im)

brightness_pixels = get_brightnessMatrix(pixels)

print(brightness_pixels)
