from master.ascii_image import *
from master.utilities import ArgumentParser
from master.fabrics import ExceptionsFabric


def main():
    argument_parser = ArgumentParser()
    args = argument_parser.get_arguments()
    image_path = args.image_path
    path_to_save = args.save
    is_coloured = args.colour

    image_processor = ImageProcessor()
    ascii_converter = ASCIIConverter()
    colour_converter = ASCIIColourConverter()
    art_handler = ASCIIArtHandler(is_coloured)
    exceptions = ExceptionsFabric().get_exceptions()

    try:
        image = art_handler.load_image(image_path)
        size = image_processor.handle_size(image, args.size)
        if args.colour:
            rgb_image = image_processor.convert_to_rgb(image, size)
            coloured_data = colour_converter.pixels_to_coloured_ascii(
                rgb_image, args.invert)
            ascii_art = colour_converter.create_coloured_ascii_art(
                coloured_data,
                size)
        else:
            gray_image = image_processor.convert_to_grayscale(image, size)
            ascii_data = ascii_converter.pixels_to_ascii(gray_image,
                                                         args.invert)
            ascii_art = ascii_converter.create_ascii_art(ascii_data, size)
        if path_to_save:
            art_handler.save_to_file(ascii_art, path_to_save)
        ASCIIArtViewer(ascii_art, size, is_coloured)
    except exceptions as e:
        print(f"\n\033[91m{e}\033[0m\n")


if __name__ == "__main__":
    main()
