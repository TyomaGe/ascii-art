import os
from PIL import Image, UnidentifiedImageError
from master.models.exceptions import WrongPathException, InvalidImageException


class ASCIIArtHandler:
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

    def save_to_file(self, ascii_art, path):
        if not path.lower().endswith('.txt'):
            raise WrongPathException(f"Path {path} must point to a txt file")
        try:
            with open(path, 'w') as file:
                file.write(ascii_art)
                print(f"\033[92mArt is saved successfully\033[0m\n")
        except IOError as e:
            raise WrongPathException(f"Could not write to file {path}") from e
