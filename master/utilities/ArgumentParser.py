import argparse


class ArgumentParser:
    def __init__(self):
        description = (
            "Convert images to ASCII art. The program processes standard "
            "image formats (JPG, PNG, etc.)\nby converting each pixel to "
            "a corresponding ASCII character,\nproducing art that can be "
            "saved as a text file."
        )
        epilog = (
            "Examples:\n"
            "  python -m master.core.main ./image.jpg "
            "./output.txt\n"
            "  python -m master.core.main ./image.png "
            "./output.txt --size 720 480\n"
        )
        self.parser = argparse.ArgumentParser(
                description=description,
                epilog=epilog,
                formatter_class=argparse.RawDescriptionHelpFormatter
        )

    def get_arguments(self):
        self.parser.add_argument(
            "image_path",
            type=str,
            help="You need to specify the full path to the image"
        )
        self.parser.add_argument(
            "path_to_save",
            type=str,
            help="You need to specify the path where to save the art"
        )
        self.parser.add_argument(
            "--size",
            nargs=2,
            metavar=("WIDTH", "HEIGHT"),
            default=None,
            help="Define new image width and height"
        )
        self.parser.add_argument(
            "--invert",
            action="store_true",
            help="Invert ASCII art (negative effect)"
        )
        arguments = self.parser.parse_args()
        return arguments
