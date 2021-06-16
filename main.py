from PIL import Image
import requests
import io
import os
import argparse
import sys
from imgconv import resize, convert_to_ascii
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
    img = None

    try:
        r = requests.head(args.input)
        if r.ok:
            r = requests.get(args.input)
            img = Image.open(io.BytesIO(r.content))
    except requests.exceptions.MissingSchema as err:
        if os.path.isfile(args.input):
            img = Image.open(args.input)
        else:
            sys.exit("Error: Unable to locate file")
    
    img = resize(img)
    ascii_art = convert_to_ascii(img, args.complex, args.negative, args.color)
    result = "\n".join([''.join(ascii_art[i:i+img.size[0]]) for i in range(0, len(ascii_art), img.size[0])])
    print(result)

    if args.output and args.output[-4:] == ".txt":
        f = open(args.output, "w")
        if args.color:
            result = regex.sub(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]", "", result)
        
        f.write(result)
        f.close()
    else:
        print("Error, the specified save file is not a text file")

    img.close()

if __name__ == '__main__':
    main()