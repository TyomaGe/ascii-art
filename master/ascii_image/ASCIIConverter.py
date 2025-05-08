class ASCIIConverter:
    __ASCII_CHAR = list(' .",:;!~+-xmo*#W&8@')

    def pixels_to_ascii(self, image):
        pixels = image.getdata()
        proportion = 255 // len(self.__ASCII_CHAR) + 1
        characters = "".join(
            self.__ASCII_CHAR[pixel // proportion] for pixel in pixels)
        return characters

    def create_ascii_art(self, image_data, size):
        pixel_count = len(image_data)
        width = size[0]
        return "\n".join(
            image_data[i:i + width] for i in range(0, pixel_count, width))
