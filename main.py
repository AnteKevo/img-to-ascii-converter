from PIL import Image
import requests
import io
import os
import argparse
import sys
from imgconv import resize, convert_to_ascii
from file_handling import extract_img, save_img
import regex

# Parser manages the arguments and captures arguments sent into the script
parser = argparse.ArgumentParser(description="Converts images into ASCII art")
parser.add_argument("input", type=str, help="The image you wish to convert")
parser.add_argument("-o", "--output", type=str, help="Saves the ASCII image in a .txt-file")
parser.add_argument("-n", "--negative", help="Creates a negative ASCII image", action="store_true")
parser.add_argument("-c", "--color", help="Attempts to color the ASCII characters if the image supports RGB", action="store_true")
parser.add_argument("-C", "--complex", help="Uses a longer ASCII sequence which represents 70 levels of gray", action="store_true")
args = parser.parse_args()

def main():
    try:
        img = resize(extract_img(args.input))
        ascii_art = convert_to_ascii(img, args.complex, args.negative, args.color)
        result = "\n".join([''.join(ascii_art[i:i+img.size[0]]) for i in range(0, len(ascii_art), img.size[0])])
        print(result)
        if args.output:
            save_img(args.output, result, args.color)
        img.close()
    except FileNotFoundError as f_not_found_err:
        print("Error! File not Found")
    except ConnectionError as con_err:
        print("Error! URL is not valid")
if __name__ == '__main__':
    main()