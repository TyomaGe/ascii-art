import argparse


class ArgumentParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()

    def get_arguments(self):
        self.parser.add_argument("image_path", type=str)
        self.parser.add_argument("path_to_save", type=str)
        self.parser.add_argument("-w", "--width", default=360, type=int)
        arguments = self.parser.parse_args()
        return arguments