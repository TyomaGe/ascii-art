class ASCIIConverter:
    __ASCII_CHAR = [
        '@', '#', ';', ':', ',', '"', '^', '`', '.', '~', '-', '_', '+', '=',
        '<', '>', '(', ')', '[', ']', '{', '}', '|', '\\', '/', ' '
    ]

    def pixels_to_ascii(self, image):
        pixels = image.getdata()
        characters = "".join(
            self.__ASCII_CHAR[pixel // 10] for pixel in pixels)
        return characters

    def create_ascii_art(self, image_data, width):
        pixel_count = len(image_data)
        return "\n".join(
            image_data[i:i + width] for i in range(0, pixel_count, width))
