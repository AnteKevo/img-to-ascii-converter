import requests
import os
from PIL import Image
import io
import regex
from requests.exceptions import MissingSchema

def is_url_img(img_url):
    img_formats = ["image/png", "image/jpeg"]
    try:
        r = requests.head(img_url)
        if r.status_code >= 400:
           raise ValueError

        if not r.headers["content-type"] in img_formats:
            raise ConnectionError
        
        return True
    except ConnectionError as con_err:
       raise con_err
    except MissingSchema as no_url_err:
        return False


def is_file_img(img_path):
   img_formats = [".png", ".jpeg", ".jpg"]
   return os.path.isfile(img_path) and img_path.endswith(tuple(img_formats))

def is_text_file(path):
    return os.path.isfile(path) and path.endswith(".txt")

def extract_img(path):
    if is_url_img(path):
        r = requests.get(path)
        img = Image.open(io.BytesIO(r.content))
    elif is_file_img(path):
        img = Image.open(path)
    else:
        raise FileNotFoundError

    return img

def save_img(path, ascii_art, color=False):
    if is_text_file(path):
        f = open(path, "w")
        if color:
            ascii_art = regex.sub(r"(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]", "", ascii_art)
        
        f.write(ascii_art)
        f.close()
    else:
        raise FileNotFoundError