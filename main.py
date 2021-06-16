import argparse

from requests.exceptions import HTTPError
from imgconv import img_to_ascii
from file_handling import extract_img, save_img

# Parser manages the arguments and captures arguments sent into the script
parser = argparse.ArgumentParser(description="Converts images into ASCII art")
parser.add_argument("input", type=str, help="The image you wish to convert")
parser.add_argument("-o", "--output", type=str, help="Saves the ASCII image in a .txt-file")
parser.add_argument("-n", "--negative", help="Creates a negative ASCII image", action="store_true")
parser.add_argument("-d", "--dimension", nargs=2, type=int, help="Creates an ASCII image with set dimensions")
parser.add_argument("-c", "--color", help="Attempts to color the ASCII characters if the image supports RGB", action="store_true")
parser.add_argument("-C", "--complex", help="Uses a longer ASCII sequence which represents 70 levels of gray", action="store_true")
parser.add_argument("-x", "--flipX", help="Flips the ASCII image from left to right", action="store_true")
parser.add_argument("-y", "--flipY", help="Flips the ASCII image from top to bottom", action="store_true")
args = parser.parse_args()

def main():
    try:
        img = extract_img(args.input)
        result = img_to_ascii(img, args.complex, args.negative, args.color, args.flipX, args.flipY, args.dimension)
        print(result)

        if args.output:
            save_img(args.output, result, args.color)

        img.close()

    except FileNotFoundError:
        print("Error! File not Found")

    except ConnectionError:
        print("Error! URL is not valid")

    except HTTPError:
        print("Error! URL image is not accessible")

    except ValueError:
        print("Error! Dimensions cannot be 0")
        
if __name__ == '__main__':
    main()