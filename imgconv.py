import os
from PIL import Image
import math

# Retrieved from http://paulbourke.net/dataformats/asciiart/
ASCII_CHARS_S = " .:-=+*#%@"
ASCII_CHARS_C = " .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

class RGBPixel:
    def __init__(self, r, g, b, complex, negative):
        self.r = 255 - r if negative else r
        self.g = 255 - g if negative else g
        self.b = 255 - b if negative else b
        self.grayscale = int(0.299*r + 0.587*g + 0.114*b)
        self.value = ASCII_CHARS_C[int((self.grayscale) // (256 / 70))] if complex else ASCII_CHARS_S[int(self.grayscale // (256 / 10))]

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


def convert_to_ascii(img, complex, negative, color):
    if color:
        if img.mode == "RGB" or img.mode == "RGBA":
            pixels = Image.Image.getdata(img)
            ascii_pixels = [RGBPixel(*pixel[:3], complex, negative) for pixel in pixels]
            return list(map(lambda a_c: f"\033[38;2;{a_c.r};{a_c.g};{a_c.b}m{a_c.value}\033[0m", ascii_pixels))
        else:
            print("Error! Image is not in RGB format")
    pixels = Image.Image.getdata(img.convert("L"))
    if negative:
        return [ASCII_CHARS_C[int((255 - pixel) // (256 / 70))] if complex else ASCII_CHARS_S[int((255 - pixel) // (256 / 10))] for pixel in pixels]
    return [ASCII_CHARS_C[int(pixel // (256 / 70))] if complex else ASCII_CHARS_S[int(pixel // (256 / 10))] for pixel in pixels]