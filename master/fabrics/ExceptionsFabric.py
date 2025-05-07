from master.models.exceptions import *
from PIL import UnidentifiedImageError


class ExceptionsFabric:
    def get_exceptions(self):
        return (
            UnidentifiedImageError,
            WrongPathException,
            WrongImageWidthException,
            WrongImageHeightException,
            InvalidSizeValueException,
            InvalidImageException
        )