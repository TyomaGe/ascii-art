import pytest
from PIL import Image
from master.ascii_image import ASCIIColourConverter


class TestASCIIColourConverter:
    @pytest.fixture
    def handler(self):
        return ASCIIColourConverter()

    @pytest.fixture
    def image(self):
        image = Image.new("RGB", (2, 2))
        image.putdata([
            (0, 0, 0),
            (85, 85, 85),
            (170, 170, 170),
            (255, 255, 255)
        ])
        return image

    def test_pixels_to_coloured_ascii_inversion(self, handler, image):
        normal = handler.pixels_to_coloured_ascii(image, invert=False)
        inverted = handler.pixels_to_coloured_ascii(image, invert=True)
        assert normal != inverted
        assert normal[0] != inverted[0]

    def test_pixels_to_coloured_ascii_caching(self, handler):
        image = Image.new("RGB", (2, 2), color=(100, 150, 200))
        result = handler.pixels_to_coloured_ascii(image)
        assert result[0] == result[1] == result[2] == result[3]

    def test_create_coloured_ascii_art_structure(self, handler):
        dummy_spans = ['<span style="color: rgb(0,0,0)">@</span>'] * 6
        size = (3, 2)
        expected = (
            "<span style=\"color: rgb(0,0,0)\">@</span>" * 3 + "<br>" +
            "<span style=\"color: rgb(0,0,0)\">@</span>" * 3
        )
        result = handler.create_coloured_ascii_art(dummy_spans, size)
        assert result == expected
