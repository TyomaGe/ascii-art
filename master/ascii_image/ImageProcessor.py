class ImageProcessor:
    def __resize_image(self, image, new_width):
        width, height = image.size
        ratio = height / (width * 2)
        new_height = int(new_width * ratio)
        return image.resize((new_width, new_height))

    def convert_to_grayscale(self, image, new_width):
        resized_image = self.__resize_image(image, new_width)
        return resized_image.convert("L")
