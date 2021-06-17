import os
from PIL import Image

# Retrieved from http://paulbourke.net/dataformats/asciiart/
ASCII_CHARS_S = " .:-=+*#%@"
ASCII_CHARS_C = " .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

class RGBPixel(object):
    def __init__(self, complex, negative, r, g, b, a=255):
        self.r = 255 - r if negative else r
        self.g = 255 - g if negative else g
        self.b = 255 - b if negative else b
        self.grayscale = int(0.299*r + 0.587*g + 0.114*b) * a
        self.value = ASCII_CHARS_C[int((self.grayscale / 65536) * len(ASCII_CHARS_C))] if complex else ASCII_CHARS_S[int((self.grayscale / 65536) * len(ASCII_CHARS_S))]

class LuminancePixel(object):
    def __init__(self, complex, negative, l, a=255):
        self.grayscale = (255 - l) * a if negative else l * a
        self.value = ASCII_CHARS_C[int((self.grayscale / 65536) * len(ASCII_CHARS_C))] if complex else ASCII_CHARS_S[int((self.grayscale / 65536) * len(ASCII_CHARS_S))]

def resize(img, flipX, flipY, dimension):
    if dimension != None:
        if dimension[0] > 0 and dimension[1] > 0:
            dimension[0] *= 2
            return img.resize(tuple(dimension), Image.LANCZOS)
        else:
            raise ValueError

    if flipX:
        img = img.transpose(Image.FLIP_LEFT_RIGHT)

    if flipY:
        img = img.transpose(Image.FLIP_TOP_BOTTOM)

    t_size = os.get_terminal_size()
    w, h = img.size
    ratio = w / h
    a_h = t_size.lines - 1
    a_w = 2 * int(ratio * a_h)

    if a_w > t_size.columns:
        a_w = t_size.columns - 1
        a_h = int(0.5 * t_size.columns / ratio)

    return img.resize((a_w, a_h), Image.LANCZOS)


def img_to_ascii(img, complex, negative, color, flipX, flipY, dimension):
    img = resize(img, flipX, flipY, dimension)
    n_w = img.size[0]
    ascii_pixels = pixels_to_ascii(img, complex, negative, color)
    return "\n".join([''.join(ascii_pixels[i:i+n_w]) for i in range(0, len(ascii_pixels), n_w)])
    

def pixels_to_ascii(img, complex, negative, color):

    if color:
        
        if img.mode == "RGB" or img.mode == "RGBA":
            pixels = Image.Image.getdata(img)
            ascii_pixels = [RGBPixel(complex, negative, *pixel) for pixel in pixels]
            return list(map(lambda a_c: f"\033[38;2;{a_c.r};{a_c.g};{a_c.b}m{a_c.value}\033[0m", ascii_pixels))
            
        else:
            print("Error! Image does not support RGB colors, printing in black and white...")

    pixels = Image.Image.getdata(img.convert("LA"))
    ascii_pixels = [LuminancePixel(complex, negative, *pixel) for pixel in pixels]
    return list(map(lambda a_c: a_c.value, ascii_pixels))