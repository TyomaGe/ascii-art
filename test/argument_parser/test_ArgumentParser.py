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

    def test_get_arguments_with_invert_flag(self, parser):
        with patch('argparse.ArgumentParser.parse_args') as mock_parse:
            mock_parse.return_value = argparse.Namespace(
                image_path="image.jpg",
                path_to_save="output.txt",
                size=None,
                invert=True
            )
            args = parser.get_arguments()
            assert args.image_path == "image.jpg"
            assert args.path_to_save == "output.txt"
            assert args.size is None
            assert args.invert is True

    def test_get_arguments_with_all_flags(self, parser):
        with patch('argparse.ArgumentParser.parse_args') as mock_parse:
            mock_parse.return_value = argparse.Namespace(
                image_path="image.jpg",
                path_to_save="output.txt",
                size=("150", "300"),
                invert=True
            )
            args = parser.get_arguments()
            assert args.image_path == "image.jpg"
            assert args.path_to_save == "output.txt"
            assert args.size == ("150", "300")
            assert args.invert is True
