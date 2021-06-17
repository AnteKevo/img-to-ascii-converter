# Copyright 2021 Antonio Kevo
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
from requests.exceptions import HTTPError
from imgconv import img_to_ascii
from file_handling import extract_data, save_img, InvalidFileExtension
import time

# Parser manages the arguments and captures arguments sent into the script
parser = argparse.ArgumentParser(prog="img-to-ascii", description="Converts images into ASCII art")
parser.add_argument("input", type=str, help="The image you wish to convert")
parser.add_argument("-o", "--output", type=str, help="Saves the ASCII image in a .txt-file")
parser.add_argument("-n", "--negative", help="Creates a negative ASCII image", action="store_true")
parser.add_argument("-d", "--dimension", nargs=2, metavar=("w","h"), type=int, help="Creates an ASCII image with set dimensions. Note: GIF-Files are not resizable")
parser.add_argument("-c", "--color", help="Attempts to color the ASCII characters if the image supports RGB. Note: GIF-Files are currently not colorable", action="store_true")
parser.add_argument("-C", "--complex", help="Uses a longer ASCII sequence which represents 70 levels of gray", action="store_true")
parser.add_argument("-x", "--flipX", help="Flips the ASCII image on the x-axis (left to right)", action="store_true")
parser.add_argument("-y", "--flipY", help="Flips the ASCII image on the y-axis (top to bottom)", action="store_true")
parser.add_argument("-g", "--gif", help="Creates ASCII frames that animates in the terminal", action="store_true")
args = parser.parse_args()

def main():
    try:
        if args.gif:
            gif = extract_data(args.input, True)

            if args.dimension:
                print("Error! GIF-files cannot be resized!")

            frames = []
            for frame in range(gif.n_frames):
                gif.seek(frame)
                result = img_to_ascii(gif, args.complex, args.negative, False, args.flipX, args.flipY, None)
                frames.append(result)

            for i in range(5):
                for frame in frames:
                    print("\033[H\033[J") # ANSI Escape Code which moves the cursor to top left of the terminal and deletes everything below
                    print(frame)
                    time.sleep(1 / 15) # 15 FPS
            
        else:
            img = extract_data(args.input)
            result = img_to_ascii(img, args.complex, args.negative, args.color, args.flipX, args.flipY, args.dimension)
            print(result)

            if args.output:
                save_img(args.output, result, args.color)

            img.close()

    except FileNotFoundError:
        print("Error! File not found or is not a .jpg/.jpeg/.png-file")

    except ConnectionError:
        print("Error! URL is not valid")

    except HTTPError:
        print("Error! URL image is not accessible")

    except ValueError:
        print("Error! Dimensions need to be 1 or greater")

    except InvalidFileExtension:
        print("Error! Invalid file extension, use a .txt-file")
        
if __name__ == '__main__':
    main()