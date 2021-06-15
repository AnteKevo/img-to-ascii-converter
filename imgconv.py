import os
from PIL import Image
import math

# Retrieved from http://paulbourke.net/dataformats/asciiart/
ASCII_CHARS_S = "@%#*+=-:. "
ASCII_CHARS_C = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{\}[]?-_+~<>i!lI;:,\"\^`'. "        

def resize(img):
    t_size = os.get_terminal_size()
    w, h = img.size
    ratio = w / h
    a_h = t_size.lines - 1
    a_w = 2 * int(ratio * a_h)

    if a_w > t_size.columns:
        a_w = t_size.columns - 1
        a_h = int(0.5 * t_size.columns / ratio)

    return img.resize((a_w, a_h), Image.LANCZOS)


def convert_to_ascii(img, complex, negative):
    pixels = Image.Image.getdata(img.convert("L"))
    if negative:
        return ''.join([ASCII_CHARS_C[math.ceil((255 - pixel) // (256 / 70))] if complex else ASCII_CHARS_S[math.ceil((255 - pixel) // (256 / 10))] for pixel in pixels])
    return ''.join([ASCII_CHARS_C[math.ceil(pixel // (256 / 70))] if complex else ASCII_CHARS_S[math.ceil(pixel // (256 / 10))] for pixel in pixels])