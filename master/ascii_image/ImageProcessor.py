from PIL import Image

from master.models.exceptions import *


class ImageProcessor:
    def __resize_image(self, image, new_size):
        return image.resize(new_size, Image.Resampling.LANCZOS)

    def convert_to_grayscale(self, image, size):
        resized_image = self.__resize_image(image, size)
        return resized_image.convert("L")

    def handle_size(self, image, size):
        if size is None:
            return image.size
        try:
            width = int(size[0])
            height = int(size[1])
        except (ValueError, TypeError):
            raise InvalidSizeValueException(
                "Width and height must be integers")

        if width <= 0:
            raise WrongImageWidthException("Width must be positive")
        if height <= 0:
            raise WrongImageHeightException("Height must be positive")
        return width, height
