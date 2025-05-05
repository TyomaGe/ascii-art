from master.ascii_image import ASCIIArtHandler, ASCIIConverter, ImageProcessor
from master.utilities import ArgumentParser
from master.models.exceptions import *


def main():
    argument_parser = ArgumentParser()
    image_processor = ImageProcessor()
    ascii_converter = ASCIIConverter()
    art_handler = ASCIIArtHandler()

    args = argument_parser.get_arguments()
    image_path = args.image_path
    path_to_save = args.path_to_save

    try:
        image = art_handler.load_image(image_path)
        size = image_processor.handle_size(image, args.size)
        gray_image = image_processor.convert_to_grayscale(image, size)
        ascii_data = ascii_converter.pixels_to_ascii(gray_image)
        ascii_art = ascii_converter.create_ascii_art(ascii_data, size)
        art_handler.save_to_file(ascii_art, path_to_save)
    except WrongImageWidthException as e:
        print(e)
    except WrongImageHeightException as e:
        print(e)


if __name__ == "__main__":
    main()
