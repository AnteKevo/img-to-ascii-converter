from PIL import Image

ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1\{\}[]?-_+~<>i!lI;:,\"^`'. "

def main(new_width = 150):
    path = input("Enter image path: ")
    img = Image.open(path)
    new_image_data = pixels_to_ascii(grayify(resize(img, new_width)))
    ascii_image = "\n".join([new_image_data[i:i+new_width] for i in range(0, len(new_image_data), new_width)])
    f = open("output.txt", "w")
    f.write(ascii_image)
    f.close()
    
def resize(img, new_width):
    width, height = img.size
    return img.resize((new_width, int(new_width * (height / width))))

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
    return "".join([ASCII_CHARS[pixel[0] // 4] for pixel in pixels])


if __name__ == '__main__':
    main()