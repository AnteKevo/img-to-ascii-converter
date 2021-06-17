import requests
import os
from PIL import Image
import io
import regex
from requests.exceptions import MissingSchema, HTTPError

class InvalidFileExtension(Exception):
    pass

def get_header(url):
    try:
        r = requests.head(url)
        if r.status_code >= 400:
            raise HTTPError

        return r.headers

    except MissingSchema:
        return None


def is_url(url, formats):
    head = get_header(url)

    if head is None:
        return False

    if not head["content-type"] in formats:
        raise ConnectionError

    return True

def is_file(path, formats):
   return os.path.isfile(path) and path.endswith(formats)

def extract_data(path, is_gif=False):
    if (is_gif and is_url(path, ["image/gif"])) or is_url(path, ["image/png", "image/jpeg"]):
        r = requests.get(path)
        data = Image.open(io.BytesIO(r.content))
    
    elif (is_gif and is_file(path, (".gif", ))) or is_file(path, (".jpg", ".jpeg", ".png")):
        data = Image.open(path)

    else:
        raise FileNotFoundError

    return data

def save_img(path, ascii_art, color):
    if path.endswith(".txt"):
        f = open(path, "w")

        if color:
            ascii_art = regex.sub(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]", "", ascii_art)
        
        f.write(ascii_art)
        f.close()

    else:
        raise InvalidFileExtension 