# Program to Find the Size (Resolution) of an Image:
import PIL    # PIL = pillow
from PIL import Image

img = PIL.Image.open("D:/Python Coding/Python Programs/42-python.png")

width, height = img.size

print(width, "x",height)