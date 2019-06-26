import json
import requests
import graphics
import matplotlib
from turtle import *
from PIL import Image, ImageFilter
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
import cv2

# print(cv2.__file__)

base_link = "https://api.noopschallenge.com/hexbot?count="

def get_colors(number_of_colors):
    if number_of_colors < 1:
        return "Your number of colors was invalid!"
    else:
        response = requests.get(base_link + str(int(number_of_colors)))
        data = response.json()
        data = data["colors"]
        list_of_hex = []
        for x in data:
            list_of_hex.append(x.get("value"))
        return list_of_hex

print(get_colors(2))

# print(type(data))
# print(data)
# print(type(data[0]))
# print(data[0])
# print(data[0].get("value"))
# for x in data:


# plt.imshow(blue)


# Blur an image
# rustom = Image.open("Rustom.jpeg")
# rustom_blurred = rustom.filter(ImageFilter.BLUR)
# rustom.show()
# rustom_blurred.show()
