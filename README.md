# Image to ASCII converter

Image to ASCII converter is a CLI tool that converts images into ASCII art printed onto the terminal.
It is cross-platform so both Windows and Linux distributions are supported.

Image formats currently supported:
* JPEG/JPG
* PNG
* GIF

## Table of Content

-   [Installation](#installation)
    * [Linux (binaries)](#linux)
	* [Windows (binaries)](#windows)
-   [CLI Usage](#cli-usage)
    * [Flags](#flags)
<!--   [Library Usage](#library-usage) -->
-   [Contributing](#contributing)
-   [Packages Used](#packages-used)
-   [License](#license)

## Installation

### Linux
Download the archive for Linux [here](https://github.com/AnteKevo/img-to-ascii-converter/releases/latest), extract it, and open the extracted directory.

Now, open a terminal in the same directory and execute this command:

```
sudo cp img-to-ascii /usr/local/bin/
```
Now you can use img-to-ascii in the terminal. Execute `img-to-ascii -h` for more details.

### Windows

You will need to set an Environment Variable to the folder the aimg-to-ascii.exe executable is placed in to be able to use it in the command prompt. Follow the instructions in case of confusion:

Download the archive for Windows [here](https://github.com/AnteKevo/img-to-ascii-converter/releases/latest), extract it, and open the extracted folder. Now, copy the folder path from the top of the file explorer and follow these instructions:
* In Search, search for and then select: System (Control Panel)
* Click the Advanced System settings link.
* Click Environment Variables. In the section User Variables find the Path environment variable and select it. Click "Edit".
* In the Edit Environment Variable window, click "New" and then paste the path of the folder that you copied initially.
* Click "Ok" on all open windows.

Now, restart any open command prompt and execute `img-to-ascii -h` for more details.

## CLI Usage

Note: Decrease font size or increase terminal width (like zooming out) for maximum quality ascii art. However do not zoom out all the way out when trying to print a GIF-file WITH color (without color should work as intended) as currently there is a bug where the ANSI Escape Codes for coloring take too long to print, resulting in poor animation.

The basic usage for converting an image into ascii art is as follows. Both paths and urls are valid.

```
img-to-ascii [path/url]
```

Example:

```
img-to-ascii example.png
```

### Flags

#### --color OR -c
Note: The description using the --help flag says that GIF coloring is not supported which is incorrect.

Display ascii art with the colors from original image. Works with the --negative flag as well. 

```
img-to-ascii -c [path/url]
# Or
img-to-ascii --color [path/url]
```

#### --complex OR -C
Print the image with a wider array of ascii characters for more detailed lighting density. Sometimes improves accuracy.

```
img-to-ascii -C [path/url]
# Or
img-to-ascii --complex [path/url]
```

#### --dimension OR -d
Note: Don't immediately append another flag with -d

Set the width and height for ascii art in CHARACTER lengths.

```
img-to-ascii -d <width> <height> [path/url]
# Or
img-to-ascii --dimension <width> <height> [path/url]
```

Example:
```
img-to-ascii -d 100 60 [path/url]
```

#### --negative OR -n
Display ascii art in negative colors. Works with both uncolored and colored text from --color flag.

```
img-to-ascii -n [path/url] 
# Or
img-to-ascii --negative [path/url]
```

#### --flipX OR -x
Flip the ascii art horizontally on the terminal.

```
img-to-ascii -x [path/url] 
# Or
img-to-ascii --flipX [path/url]
```

#### --flipY OR -y
Flip the ascii art vertically on the terminal.

```
img-to-ascii -y [path/url] 
# Or
img-to-ascii --flipY [path/url]
```

#### --gif OR -g
Note: The specified path or url has to contain a gif-file. --dimension cannot be used along with GIF-files.

Animates a GIF-file in the terminal.
```
img-to-ascii -g [gif path/url] 
# Or
img-to-ascii --gif [gif path/url]
```

#### --output OR -o
Note: If used with --color, it will not save the image with color. It will also not save GIF-files.

Saves an ASCII Image in a .txt-file.
```
img-to-ascii -o <path/to/txt-file> [path/url] 
# Or
img-to-ascii --output <path/to/txt-file> [path/url]
```

<!-- ## Library Usage

WIP -->

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Packages Used

[https://github.com/psf/requests](https://github.com/psf/requests)

[https://pypi.org/project/regex/](https://pypi.org/project/regex/)

[https://github.com/python-pillow/Pillow](https://github.com/python-pillow/Pillow)

## License

[Apache 2.0](https://github.com/AnteKevo/img-to-ascii-converter/blob/main/LICENSE)




