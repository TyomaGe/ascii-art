from master.utilities import ASCII_CHAR


class ASCIIConverter:
    def __init__(self):
        self.__ascii_chars = ASCII_CHAR
        self.__inverted_chars = list(reversed(self.__ascii_chars))

    def pixels_to_ascii(self, image, invert=False):
        pixels = image.getdata()
        proportion = 255 // (len(self.__ascii_chars) - 1)
        chars = self.__inverted_chars if invert else self.__ascii_chars
        return "".join(
            chars[min(pixel // proportion, len(chars) - 1)] for pixel in
            pixels)

    def create_ascii_art(self, image_data, size):
        pixel_count = len(image_data)
        width = size[0]
        return "\n".join(
            image_data[i:i + width] for i in range(0, pixel_count, width))
