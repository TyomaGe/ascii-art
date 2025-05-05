import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

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
            default=None,
            help="First argument is width. Second argument is height"
        )
        arguments = self.parser.parse_args()
        return arguments
