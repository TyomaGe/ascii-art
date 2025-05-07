class WrongPathException(Exception):
    def __init__(self, message="The file path is incorrect"):
        super().__init__(message)


class WrongImageWidthException(Exception):
    def __init__(self, message="The specified value is invalid"):
        super().__init__(message)


class WrongImageHeightException(Exception):
    def __init__(self, message="The specified value is invalid"):
        super().__init__(message)


class InvalidSizeValueException(Exception):
    def __init__(self, message="The specified value is invalid"):
        super().__init__(message)


class InvalidImageException(Exception):
    def __init__(self, message="The specified file is not an image"):
        super().__init__(message)
