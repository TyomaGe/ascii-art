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
        try:
            with open(path, "w") as file:
                file.write(ascii_art)
        except WrongPathException(f"The path: {path} is incorrect") as e:
            print(e)
