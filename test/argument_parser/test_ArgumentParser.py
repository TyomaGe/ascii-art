import argparse
import pytest
from unittest.mock import patch
from master.utilities import ArgumentParser


class TestArgumentParser:
    @pytest.fixture
    def parser(self):
        return ArgumentParser()

    def test_get_arguments_returns_two_args(self, parser):
        with patch('argparse.ArgumentParser.parse_args') as mock_parse:
            mock_parse.return_value = argparse.Namespace(
                image_path="image.jpg",
                path_to_save="output.txt",
                size=None
            )
            args = parser.get_arguments()
            assert args.image_path == "image.jpg"
            assert args.path_to_save == "output.txt"
            assert args.size is None

    def test_get_arguments_returns_three_args(self, parser):
        with patch('argparse.ArgumentParser.parse_args') as mock_parse:
            mock_parse.return_value = argparse.Namespace(
                image_path="image.jpg",
                path_to_save="output.txt",
                size=("100", "200")
            )
            args = parser.get_arguments()
            assert args.image_path == "image.jpg"
            assert args.path_to_save == "output.txt"
            assert args.size == ("100", "200")
