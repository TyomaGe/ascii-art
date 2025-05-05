from PIL import Image


class ASCIIArtHandler:
    def load_image(self, path):
        try:
            return Image.open(path)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None

    def save_to_file(self, ascii_art, filename="asciiArt.txt"):
        try:
            with open(filename, "w") as file:
                file.write(ascii_art)
        except Exception as e:
            print(f"Error saving file: {e}")
