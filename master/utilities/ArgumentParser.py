import argparse
from .config import ARGPARSE_DESCRIPTION, ARGPARSE_EPILOG


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            description=ARGPARSE_DESCRIPTION,
            epilog=ARGPARSE_EPILOG,
            formatter_class=argparse.RawDescriptionHelpFormatter
        )

    def get_arguments(self):
        self.parser.add_argument(
            "image_path",
            type=str,
            help="You need to specify the full path to the image"
        )
        self.parser.add_argument(
            "-sv", "--save",
            default=None,
            type=str,
            help="You need to specify the path where to save the art"
        )
        self.parser.add_argument(
            "-s", "--size",
            nargs=2,
            metavar=("WIDTH", "HEIGHT"),
            default=None,
            help="Define new image width and height"
        )
        self.parser.add_argument(
            "-i", "--invert",
            action="store_true",
            help="Invert ASCII-Art (negative effect)"
        )
        self.parser.add_argument(
            "-c", "--colour",
            action="store_true",
            help="Generate coloured ASCII-Art"
        )
        arguments = self.parser.parse_args()
        return arguments
