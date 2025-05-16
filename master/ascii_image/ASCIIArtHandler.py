import os
from PIL import Image, UnidentifiedImageError
from master.models.exceptions import WrongPathException, InvalidImageException
from master.utilities import HTML_TEMPLATE


class ASCIIArtHandler:
    def __init__(self, is_coloured=False):
        self.__is_coloured = is_coloured

    def load_image(self, path):
        if not os.path.exists(path):
            raise WrongPathException(f"The path: {path} is incorrect")
        try:
            img = Image.open(path)
            img.verify()
            img = Image.open(path)
            return img
        except UnidentifiedImageError as e:
            raise InvalidImageException(
                f"File {path} is not a valid image"
            ) from e

    def save_as_txt(self, ascii_art, path):
        self.__check_valid_format_matching(path)
        try:
            with open(path, 'w') as file:
                file.write(ascii_art)
                print(f"\n\033[92mArt is saved successfully\033[0m")
        except IOError as e:
            raise WrongPathException(f"Could not write to file {path}") from e

    def save_as_html(self, ascii_art, path):
        self.__check_valid_format_matching(path)
        try:
            html_content = HTML_TEMPLATE.format(ascii_art=ascii_art)
            with open(path, 'w') as file:
                file.write(html_content)
                print(f"\n\033[92mArt is saved successfully\033[0m")
        except IOError as e:
            raise WrongPathException(f"Could not write to file {path}") from e

    def __check_valid_format_matching(self, path):
        if self.__is_coloured:
            if not path.lower().endswith('.html'):
                raise WrongPathException(
                    f"Path {path} must point to a html file (coloured art)")
        else:
            if not path.lower().endswith('.txt'):
                raise WrongPathException(
                    f"Path {path} must point to a txt file (gray art)")
