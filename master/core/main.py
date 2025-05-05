from master.ascii_image import ASCIIArtHandler, ASCIIConverter, ImageProcessor
from master.utilities import ArgumentParser


def main():
    argument_parser = ArgumentParser()
    image_processor = ImageProcessor()
    ascii_converter = ASCIIConverter()
    art_handler = ASCIIArtHandler()

    args = argument_parser.get_arguments()
    path = args.image_path
    path_to_save = args.path_to_save
    optimal_width = args.width

    image = art_handler.load_image(path)
    gray_image = image_processor.convert_to_grayscale(image, optimal_width)
    ascii_data = ascii_converter.pixels_to_ascii(gray_image)
    ascii_art = ascii_converter.create_ascii_art(ascii_data, optimal_width)
    art_handler.save_to_file(ascii_art, path_to_save)

if __name__ == "__main__":
    main()
