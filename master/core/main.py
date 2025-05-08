from master.ascii_image import *
from master.utilities import ArgumentParser
from master.fabrics import ExceptionsFabric


def main():
    argument_parser = ArgumentParser()
    image_processor = ImageProcessor()
    ascii_converter = ASCIIConverter()
    art_handler = ASCIIArtHandler()
    exceptions = ExceptionsFabric().get_exceptions()

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
        ASCIIArtViewer(ascii_art, size)

    except exceptions as e:
        print(f"\n\033[91m{e}\033[0m\n")


if __name__ == "__main__":
    main()
