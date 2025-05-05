from PIL import Image
from master.models.exceptions import WrongPathException


class ASCIIArtHandler:
    def load_image(self, path):
        try:
            return Image.open(path)
        except WrongPathException as e:
            print(e)
            return None

    def save_to_file(self, ascii_art, filename="asciiArt.txt"):
        try:
            with open(filename, "w") as file:
                file.write(ascii_art)
        except WrongPathException("The specified path is incorrect") as e:
            print(e)
