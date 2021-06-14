from PIL import Image
import os

ASCII_CHARS = "@%#*+=-:. "

def main():
    t_line = os.get_terminal_size().lines - 1
    path = input("Enter image path: ")
    try:
        img = Image.open(path)
        new_img, new_w = resize(img, t_line)
        new_img_data = pixels_to_ascii(grayify(new_img))
        ascii_image = "\n".join([new_img_data[i:i+new_w] for i in range(0, len(new_img_data), new_w)])
        #f = open("output.txt", "w")
        #f.write(ascii_image)
        #f.close()
        print(ascii_image)
        img.close()
    except FileNotFoundError as fnf:
        print(fnf)
    
    except PIL.UnidentifiedImageError as err:
        print(err)
    
def resize(img, new_h):
    w, h = img.size
    ratio = w / h
    new_w = int(new_h * ratio)
    return (img.resize((new_w, new_h)), new_w)

def grayify(image):
    pixels = image.load()

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            l = int(r * 0.2126 + g * 0.7156 + b * 0.0722)

            pixels[i, j] = (l, l, l)
    return image

def pixels_to_ascii(image):
    pixels = image.getdata()
    return "".join([ASCII_CHARS[pixel[0] // 26] for pixel in pixels])


if __name__ == '__main__':
    main()