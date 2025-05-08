import pytest
from PIL import Image
from master.ascii_image import ASCIIConverter


class TestASCIIConverter:
    @pytest.fixture
    def handler(self):
        return ASCIIConverter()

    @pytest.fixture
    def image(self):
        image = Image.new("L", (2, 2))
        image.putdata([0, 85, 170, 255])
        return image

    def test_pixels_to_ascii_varied_brightness(self, handler, image):
        result = handler.pixels_to_ascii(image)
        assert len(result) == 4
        assert result[0] != result[1] != result[2] != result[3]
        assert result[0] == handler._ASCIIConverter__ASCII_CHAR[0]
        assert result[3] == handler._ASCIIConverter__ASCII_CHAR[-1]

    def test_pixels_to_ascii_char_range(self, handler, image):
        result = handler.pixels_to_ascii(image)
        valid_chars = handler._ASCIIConverter__ASCII_CHAR
        assert all(char in valid_chars for char in result)

    def test_create_ascii_art_formatting(self, handler):
        test_data = "@" * 6
        size = (3, 2)
        expected = "@@@\n@@@"
        assert handler.create_ascii_art(test_data, size) == expected

    def test_pixels_to_ascii_inverted(self, handler, image):
        original_chars = handler._ASCIIConverter__ASCII_CHAR
        inverted_chars = original_chars[::-1]
        inverted_result = handler.pixels_to_ascii(image, invert=True)
        assert inverted_result[0] == inverted_chars[0]
        assert inverted_result[-1] == inverted_chars[-1]
        normal_result = handler.pixels_to_ascii(image, invert=False)
        assert inverted_result != normal_result